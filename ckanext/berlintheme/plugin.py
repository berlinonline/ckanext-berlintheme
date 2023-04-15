# coding: utf-8

import os
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.berlintheme.helpers as theme_helpers

from ckanext.berlintheme import page_blueprint

class BerlinTheme(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    # -------------------------------------------------------------------
    # Implementation IConfigurer
    # -------------------------------------------------------------------

    def update_config(self, config):  
        our_public_dir = os.path.join('theme', 'public')
        template_dir = os.path.join('theme', 'templates')
        assets_dir = os.path.join('theme', 'assets')

        # overriding configuration fields:
        # set our local template and resource overrides
        toolkit.add_public_directory(config, our_public_dir)
        toolkit.add_template_directory(config, template_dir)

        toolkit.add_resource(assets_dir, 'berlintheme')

        config['ckan.site_logo'] = "/images/berlin_open_data.png"
        config['ckan.favicon'] = "/favicon.ico"
        config['berlin.public_pages'] = 'about datenschutzerklaerung'

    # -------------------------------------------------------------------
    # Implementation ITemplateHelpers
    # -------------------------------------------------------------------

    def get_helpers(self):
        return {
            'berlin_dataset_type_mapping': theme_helpers.dataset_type_mapping ,
            'berlin_type_mapping_select_options': theme_helpers.type_mapping_select_options ,
            'berlin_temporal_granularity_select_options': theme_helpers.temporal_granularity_select_options ,
            'berlin_geo_granularity_select_options': theme_helpers.geo_granularity_select_options ,
            'berlin_geo_coverage_select_options':
                theme_helpers.geo_coverage_select_options ,
            'berlin_state_mapping': theme_helpers.state_mapping ,
            'berlin_user_orgs': theme_helpers.organizations_for_user ,
            'berlin_is_sysadmin': theme_helpers.is_sysadmin ,
            'berlin_required': theme_helpers.required ,
            'berlin_group_select_options': theme_helpers.group_select_options ,
            'berlin_first_group_name': theme_helpers.first_group_name ,
            'berlin_show_warning': theme_helpers.show_warning ,
            'berlin_warning_text': theme_helpers.warning_text ,
        }

    # -------------------------------------------------------------------
    # IBlueprint
    # -------------------------------------------------------------------

    def get_blueprint(self):
        """
        Implementation of
        https://docs.ckan.org/en/latest/extensions/plugin-interfaces.html#ckan.plugins.interfaces.IBlueprint.get_blueprint
        """

        return page_blueprint.page_blueprint
