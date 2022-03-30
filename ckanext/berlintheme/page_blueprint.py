# encoding: utf-8

from flask import Blueprint

import ckan.lib.base as base


def privacy_policy():
    return base.render('home/privacy_policy.html')

page_blueprint = Blueprint('page_blueprint', __name__)
page_blueprint.add_url_rule(u'/datenschutzerklaerung', methods=[u'GET'], view_func=privacy_policy)

