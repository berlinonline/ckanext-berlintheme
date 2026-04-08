# coding: utf-8
"""Tests for plugin.py."""

import logging
import pytest

import ckan.logic as logic
import ckan.model as model

from ckanext.berlintheme.tests import orgs, user

PLUGIN_NAME = 'berlintheme'

LOG = logging.getLogger(__name__)
get_action = logic.get_action


@pytest.mark.ckan_config('ckan.plugins', f"{PLUGIN_NAME}")
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestPlugin(object):

    def test_privacy_policy_route_logged_in(self, app, user):
        '''Test rendering of privacy policy / Datenschutzerklärung for 
           a logged-in user.'''
        response = app.get(
            headers=[("Authorization", user.apikey)],
            url="/datenschutzerklaerung",
            status=200
        )
        assert "Datenschutzerklärung" in response.body
