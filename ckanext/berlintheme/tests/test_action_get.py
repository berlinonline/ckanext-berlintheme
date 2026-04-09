import json
import logging
import pytest

from flask import Flask

import ckan.common as c
import ckan.plugins.toolkit as toolkit
import ckan.tests.factories as factories

import ckanext.berlintheme as berlintheme
from ckanext.berlintheme.tests import sysadmin, patched_dataset, datasets, orgs

flask_app = Flask(__name__)
PLUGIN_NAME = 'berlintheme'
LOG = logging.getLogger(__name__)

@pytest.mark.ckan_config('ckan.plugins', f'{PLUGIN_NAME} stats')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestStatusShow(object):

    def test_status_show_has_versions(self, app, sysadmin):
        '''Check that the list of extensions returned from status_show includes
           their version, if available.'''

        response = app.get(
            url='/api/3/action/status_show',
            extra_environ={'Authorization': sysadmin['apikey']},
            status=200
        )

        data = json.loads(response.body)
        assert 'extensions' in data['result']
        extensions = data['result']['extensions']
        assert type(extensions) is dict
        assert 'stats' in extensions
        assert extensions['stats']['version'] == 'unknown'
        assert PLUGIN_NAME in extensions
        assert extensions[PLUGIN_NAME]['version'] == berlintheme.__version__

@pytest.mark.ckan_config('ckan.plugins', f'{PLUGIN_NAME} stats')
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestActivityDiff(object):

    def test_activity_diff_works(self, app, sysadmin, patched_dataset):
        '''Check that the HTML representation of activity_diff makes sense.'''

        # first get the list of activities for the patched dataset
        response = app.get(
            url='/api/3/action/package_activity_list',
            query_string=f"id={patched_dataset['id']}",
            extra_environ={'Authorization': sysadmin['apikey']},
            status=200
        )
        data = json.loads(response.body)
        last_activity = data['result'][0]

        # now get the diff for the first activity
        response = app.post(
            url='/api/3/action/activity_diff',
            extra_environ={'Authorization': sysadmin['apikey']},
            data={
                'id': last_activity['id'],
                'object_type': 'package',
                'diff_type': 'html'
            },
            status=200
        )
        data = json.loads(response.body)
        diff_markup = data['result']['diff']

        # is the new title in the diff?
        assert patched_dataset['title'] in diff_markup

        # does the diff include a typical div element?
        assert '<div class="diff_cell diff_current">' in diff_markup

        # does the diff not include a table element?
        assert '</table>' not in diff_markup