# encoding: utf-8

from flask import Blueprint

import ckan.lib.base as base


def privacy_policy():
    return base.render('home/privacy_policy.html')

def accessibility_statement():
    return base.render('home/accessibility_statement.html')

page_blueprint = Blueprint('page_blueprint', __name__)
page_blueprint.add_url_rule(u'/datenschutzerklaerung', methods=[u'GET'], view_func=privacy_policy)
page_blueprint.add_url_rule(u'/barrierefreiheitserklaerung', methods=[u'GET'], view_func=accessibility_statement)

