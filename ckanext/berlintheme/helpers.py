# coding: utf-8

import os
import json
import logging
import ckan.lib.helpers as h
import ckan.logic as logic
import ckan.model as model
from ckan.common import _, c, response

log = logging.getLogger(__name__)

get_action = logic.get_action
NotAuthorized = logic.NotAuthorized

_facet_mapping = {}


def read_facet_mapping():
  path = os.path.abspath(__file__)
  dir_path = os.path.dirname(path)
  with open(os.path.join(dir_path, "config", "facet_name_mapping.json")) as json_data:
    global _facet_mapping
    _facet_mapping = json.load(json_data)


def facet_mapping(item, facet):
  global _facet_mapping
  name = item['display_name']
  # log.debug("{}:{}".format(name.encode('utf-8'), facet.encode('utf-8')))
  if facet in _facet_mapping:
    if name in _facet_mapping[facet]:
      return _facet_mapping[facet][name]
  return name


def unlink_email(email):
  return email.replace("@", " AT ")


def dateformat():
  return "%d.%m.%Y"


def render_datetime(datetime):
  return h.render_datetime(datetime, date_format=dateformat())


def recent_packages(package_type="dataset", sort_by='metadata_created desc', limit=5):
  from ckan.lib.search import SearchError, SearchQueryError

  context = {'model': model, 'user': c.user,
             'auth_user_obj': c.userobj}
  data_dict = {
    'fq': ' +dataset_type:{type}'.format(type=package_type),
    'rows': limit,
    'sort': sort_by,
    'include_private': False,
  }
  try:
    query = get_action('package_search')(context, data_dict)
    return query['results']
  except SearchQueryError, se:
    # User's search parameters are invalid, in such a way that is not
    # achievable with the web interface, so return a proper error to
    # discourage spiders which are the main cause of this.
    log.info('Dataset search query rejected: %r', se.args)
    abort(400, _('Invalid search query: {error_message}')
          .format(error_message=str(se)))
  except SearchError, se:
    # May be bad input from the user, but may also be more serious like
    # bad code causing a SOLR syntax error, or a problem connecting to
    # SOLR
    log.error('Dataset search error: %r', se.args)
    c.query_error = True
    c.search_facets = {}
    c.page = h.Page(collection=[])
  except NotAuthorized:
    abort(403, _('Not authorized to see this page'))

def resource_label(resource):
  label = "Unbekannt"

  if resource['name']:
    name = resource['name']
  else:
    url = resource['url']
    name = url[url.rfind("/") + 1:].split('?')[0]

  if len(name) > 0:
    label = name

  return label
