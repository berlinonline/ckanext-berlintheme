import json
import logging
import pytest

from flask import Flask

import ckan.common as c
import ckan.plugins.toolkit as toolkit
import ckan.tests.factories as factories

import ckanext.berlintheme as berlintheme
from ckanext.berlintheme.tests import sysadmin

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
