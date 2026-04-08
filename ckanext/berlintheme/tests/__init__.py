import ckan.logic as logic
import ckan.model as model
import ckan.tests.factories as factories
import ckan.tests.helpers as core_test_helpers
import pytest

REGULORG = "regular_org"
TECHNORG = "technorg"

@pytest.fixture
def sysadmin():
    '''Fixture to create a sysadmin user.'''
    return factories.Sysadmin(name='theadmin')

@pytest.fixture
def orgs():
    '''Fixture to create some organizations.'''

    regulorg = factories.Organization(name=REGULORG, extras=[{ "key": "external", "value": True }])
    technorg = factories.Organization(name=TECHNORG)

    return {
        REGULORG: regulorg ,
        TECHNORG: technorg ,
    }

@pytest.fixture
def user(orgs):
    '''Fixture to create a logged-in user.'''
    user = model.User(name="vera_musterer", password=u"testtest")
    model.Session.add(user)
    model.Session.commit()

    org = orgs[REGULORG]
    data = {
        "id": org['id'],
        "username": user.name,
        "role": "editor"
    }
    core_test_helpers.call_action("organization_member_create", **data)

    return user


@pytest.fixture
def datasets(orgs):
    '''Fixture to create some datasets.'''

    sysadminuser = factories.Sysadmin()

    group = factories.Group()
    data = {
        "id": group['id'],
        "username": sysadminuser['name'],
        "role": "editor"
    }
    core_test_helpers.call_action("group_member_create", **data)

    org = orgs[REGULORG]
    data = {
        "id": org['id'],
        "username": sysadminuser['name'],
        "role": "editor",
    }
    core_test_helpers.call_action("organization_member_create", **data)

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
            "author": "BerlinOnline GmbH",
            "license_id": "cc-by",
            "notes": "Zugriffsstatistik des Berliner Datenportals"
            "(daten.berlin.de). Enthalten sind die Gesamtzugriffe"
            "auf die Domain daten.berlin.de('impressions' und"
            "'visits') für jeden Monat, sowie die Zugriffszahlen"
            "('impressions' und 'visits') für alle Datensätze für"
            "jeden Monat.\r\n\r\nDer Datensatz wird monatlich erneuert.",
            "groups": [
                {"name": group['name']}
            ],
            "owner_org": REGULORG,
            "hvd_category": "c_e1da4e07",
            "sample_record": "digitalisierung/openData/zugriffszahl",
        },
        {
            "name": "zugriffsstatistik-daten-berlin-de_2",
            "title": "Zugriffsstatistik daten.berlin.de",
            "berlin_source": "test",
            "berlin_type": "datensatz",
            "date_released": "2018-06-25",
            "date_updated": "2019-01-01",
            "temporal_coverage_from": "2011-09-01",
            "temporal_coverage_to": "2018-12-31",
            "maintainer_email": "opendata@berlin.de",
            "author": "BerlinOnline GmbH",
            "license_id": "cc-by",
            "notes": "Zugriffsstatistik des Berliner Datenportals"
            "(daten.berlin.de). Enthalten sind die Gesamtzugriffe"
            "auf die Domain daten.berlin.de('impressions' und"
            "'visits') für jeden Monat, sowie die Zugriffszahlen"
            "('impressions' und 'visits') für alle Datensätze für"
            "jeden Monat.\r\n\r\nDer Datensatz wird monatlich erneuert.",
            "groups": [
                {"name": group['name']}
            ],
            "owner_org": REGULORG,
        }
    ]

    for dataset_dict in dataset_dicts:
        core_test_helpers.call_action(
            "package_create",
            context={"user": sysadminuser['id']},
            **dataset_dict
        )

    return dataset_dicts

