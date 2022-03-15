# coding: utf-8
"""Sanity tests for the various view and edit templates."""

import pytest

import ckanext.berlintheme.helpers as helpers

THEME_PLUGIN = 'berlintheme'

@pytest.mark.ckan_config('ckan.plugins', f"{THEME_PLUGIN}")
@pytest.mark.usefixtures('clean_db', 'clean_index', 'with_plugins')
class TestHelpers(object):

    @pytest.mark.parametrize("data", [
        {
            "name": "a-dataset-thats-in-a-group",
            "title": "A dataset that's in a group",
            "groups": [
                    {"name": u"eine-gruppe"}
            ]
        },
        {
            "name": "a-dataset-thats-not-in-a-group",
            "title": "A dataset that's not in a group",
        },
    ])
    def test_first_group_name(self, app, data):
        if 'groups' in data:
            assert helpers.first_group_name(data) is data['groups'][0]['name']
        else:
            assert helpers.first_group_name(data) is None


