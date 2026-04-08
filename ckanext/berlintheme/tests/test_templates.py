# coding: utf-8
"""Sanity tests for the various view and edit templates."""

import pytest

from ckanext.berlintheme.tests import orgs, user, datasets, REGULORG, TECHNORG

import ckan.plugins.toolkit as toolkit
import ckan.tests.factories as factories
import ckan.tests.helpers as core_test_helpers

THEME_PLUGIN = 'berlintheme'
SCHEMA_PLUGIN = 'berlin_dataset_schema'
AUTH_PLUGIN = 'berlinauth'

@pytest.mark.ckan_config('ckan.plugins', f"{SCHEMA_PLUGIN} {THEME_PLUGIN}")
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestTemplates(object):

    def test_org_view_template(self, app, user, orgs):
        '''Sanity test of the organization view template'''

        response = app.get(
            headers=[("Authorization", user.apikey)],
            url=toolkit.url_for('organization.read', id=orgs[REGULORG]['id']),
            status=200
        )
        assert orgs[REGULORG]['title'] in response.body
        assert "(extern)" in response.body

        sysadminuser = factories.Sysadmin()
        response = app.get(
            headers=[("Authorization", sysadminuser['id'])],
            url=toolkit.url_for('organization.read', id=orgs[TECHNORG]['id']),
            status=200
        )
        assert orgs[TECHNORG]['title'] in response.body
        assert "(extern)" not in response.body


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
            assert u"Geographischer Bezug" in response.body
            assert u"Geographische Granularität" in response.body
            assert u"Zeitliche Granularität" in response.body
            assert u"Zeitlicher Bezug" in response.body


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
            assert u"Zeitraum von" in response.body

            # check presence of CSS classes
            assert u"icon-required" in response.body

    def test_user_view_template(self, app, user):
        '''Sanity test of the user view template'''
        data = {
            "id": user.id,
            "permission": "create_dataset"
        }
        result = core_test_helpers.call_action("organization_list_for_user", **data)
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
            url=toolkit.url_for('home.index'),
            status=200
        )
        assert warning_text in response.body

@pytest.mark.ckan_config('ckan.plugins', f"{SCHEMA_PLUGIN} {THEME_PLUGIN} {AUTH_PLUGIN}")
@pytest.mark.ckan_config('berlin.technical_groups', TECHNORG)
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestTemplatesWithAuth(object):

    def test_non_admin_can_see_technical_dataset(self, app, user, datasets, orgs):

        technorg = orgs[TECHNORG]
        sysadminuser = factories.Sysadmin()

        for dataset in datasets:
            core_test_helpers.call_action(
                "package_owner_org_update",
                context={"user": sysadminuser['id']},
                id=dataset['name'],
                organization_id=technorg['id']
            )

            response = app.get(
                headers=[("Authorization", user.apikey)],
                url=toolkit.url_for('dataset.read', id=dataset['name']),
                status=200
            )
            assert dataset['name'] in response.body
