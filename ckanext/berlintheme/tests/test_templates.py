# coding: utf-8
"""Sanity tests for the various view and edit templates."""

import pytest

import ckan.logic as logic
import ckan.model as model
import ckan.plugins.toolkit as toolkit
import ckan.tests.factories as factories
import ckan.tests.helpers as test_helpers

THEME_PLUGIN = 'berlintheme'
SCHEMA_PLUGIN = 'berlin_dataset_schema'

@pytest.fixture
def user():
    '''Fixture to create a logged-in user.'''
    user = model.User(name="vera_musterer", password=u"testtest")
    model.Session.add(user)
    model.Session.commit()

    org = factories.Organization()
    data = {
        "id": org['id'],
        "username": user.name,
        "role": "editor"
    }
    result = test_helpers.call_action("organization_member_create", **data)

    return user


@pytest.fixture
def datasets():
    '''Fixture to create some datasets.'''
    sysadminuser = model.User(name="admin", password=u'test', sysadmin=True)
    model.Session.add(sysadminuser)
    model.Session.commit()
    group = factories.Group()
    data = {
        "id": group['id'],
        "username": sysadminuser.name,
        "role": "editor"
    }
    result = test_helpers.call_action("group_member_create", **data)

    dataset_dicts = [
        {
            "name": "zugriffsstatistik-daten-berlin-de",
            "title": "Zugriffsstatistik daten.berlin.de",
            "berlin_source": "test",
            "berlin_type": "datensatz",
            "date_released": "2018-06-25",
            "date_updated": "2019-01-01",
            "temporal_coverage_from": "2011-09-01",
            "temporal_coverage_to": "2018-12-31",
            "maintainer_email": "opendata@berlin.de",
            "author": "BerlinOnline Stadtportal GmbH & Co. KG",
            "license_id": "cc-by",
            "notes": "Zugriffsstatistik des Berliner Datenportals"
            "(daten.berlin.de). Enthalten sind die Gesamtzugriffe"
            "auf die Domain daten.berlin.de('impressions' und"
            "'visits') für jeden Monat, sowie die Zugriffszahlen"
            "('impressions' und 'visits') für alle Datensätze für"
            "jeden Monat.\r\n\r\nDer Datensatz wird monatlich erneuert.",
            "groups": [
                {"name": group['name']}
            ]
        }
    ]

    for dataset_dict in dataset_dicts:
        test_helpers.call_action(
            "package_create",
            context={"user": sysadminuser.id},
            **dataset_dict
        )

    return dataset_dicts

@pytest.mark.ckan_config('ckan.plugins', f"{SCHEMA_PLUGIN} {THEME_PLUGIN}")
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestPlugin(object):

    def test_dataset_view_template(self, app, user, datasets):
        '''Sanity test of the dataset view template'''
        for dataset in datasets:
            response = app.get(
                headers=[("Authorization", user.apikey)],
                url=toolkit.url_for('dataset.read', id=dataset['name']),
                status=200
            )

            # check presence of metadata
            assert dataset['title'] in response.body
            assert dataset['maintainer_email'] in response.body

            # check presence of metadata attributes
            assert u"Geografische Abdeckung" in response.body
            assert u"Geografische Auflösung" in response.body
            assert u"Zeitliche Auflösung" in response.body
            assert u"Zeitliche Abdeckung von" in response.body


    def test_dataset_edit_template(self, app, user, datasets):
        '''Sanity test of the dataset edit template'''
        for dataset in datasets:
            response = app.get(
                headers=[("Authorization", user.apikey)],
                url=toolkit.url_for("dataset.edit", id=dataset['name']),
                status=200
            )

            # check presence of metadata
            assert dataset['title'] in response.body
            assert dataset['maintainer_email'] in response.body

            # check presence of metadata attributes
            assert u"Geografische Abdeckung" in response.body
            assert u"Geografische Auflösung" in response.body
            assert u"Zeitliche Auflösung" in response.body
            assert u"Zeitliche Auflösung" in response.body

            # check presence of CSS classes
            assert u"datasetform-required" in response.body

    def test_user_view_template(self, app, user):
        '''Sanity test of the user view template'''
        data = {
            "id": user.id,
            "permission": "create_dataset"
        }
        result = test_helpers.call_action("organization_list_for_user", **data)
        org = result[0]
        response = app.get(
            headers=[("Authorization", user.apikey)],
            url=toolkit.url_for("user.read", id=user.name),
            status=200
        )

        # the custom user view template lists organizations, they should be present with
        # title and link:
        assert org['display_name'] in response.body
        assert toolkit.url_for("organization.read", id=org['name']) in response.body

    def test_warning_template(self, app, user):
        '''Sanity test of the warning template'''
        from ckan.common import config

        warning_text = u"Lorem ipsum foobar dingdong."
        config['berlintheme.show_warning'] = True
        config['berlintheme.warning'] = warning_text

        response = app.get(
            headers=[("Authorization", user.apikey)],
            url=toolkit.url_for("home.index"),
            status=200
        )
        assert warning_text in response.body
        assert 'global_warning.css' in response.body
