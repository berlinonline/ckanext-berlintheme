# coding: utf-8

import os
import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.berlintheme.helpers as theme_helpers
from pylons import config

log = logging.getLogger(__name__)

class BerlinTheme(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IActions)

    # -------------------------------------------------------------------
    # Implementation IConfigurer
    # -------------------------------------------------------------------

    def update_config(self, config):  
        our_public_dir = os.path.join('theme', 'public')
        template_dir = os.path.join('theme', 'templates')

        # overriding configuration fields:
        # set our local template and resource overrides
        toolkit.add_public_directory(config, our_public_dir)
        toolkit.add_template_directory(config, template_dir)

        config['ckan.site_logo'] = "/images/berlin_open_data.png"
        config['ckan.favicon'] = "/favicon.ico"

        config['berlin.non_list_users'] = "logged_in visitor"

        config['berlintheme.breadcrumb_length'] = 60
        config['ckan.ui.group.items_per_page'] = 20


        theme_helpers.read_facet_mapping()
        theme_helpers.compile_path_patterns()

    # -------------------------------------------------------------------
    # Implementation ITemplateHelpers
    # -------------------------------------------------------------------

    def get_helpers(self):
        return {
            'berlintheme_facet_mapping': theme_helpers.facet_mapping ,
            'berlin_unlink_email': theme_helpers.unlink_email ,
            'berlin_render_datetime': theme_helpers.render_datetime ,
            'berlin_recent_packages': theme_helpers.recent_packages ,
            'berlin_resource_label': theme_helpers.resource_label ,
            'berlin_breadcrumb_length': theme_helpers.breadcrumb_length ,
            'berlin_build_menu_item': theme_helpers.build_menu_item ,
            'berlin_http_status_codes': theme_helpers.http_status_code_mapping ,
            'berlin_user_object': theme_helpers.user_object ,
            'berlin_log_this': theme_helpers.log_this ,
        }

    # -------------------------------------------------------------------
    # Implementation IActions
    # -------------------------------------------------------------------

    def get_actions(self):
        return {
            # this was meant to restrict the list of users returned
            # by user_list, but it's not working yet
            # "user_list": theme_helpers.user_list ,
        }