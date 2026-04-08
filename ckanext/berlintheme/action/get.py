# encoding: utf-8
"""Custom implementations of action functions from ckan.logic.action.get
"""

import importlib.metadata as md
import json
import logging

import ckan as ckan
import ckan.lib.dictization.model_dictize as model_dictize
import ckan.logic.action.get as ckanget
from ckan.logic import NotFound, ValidationError

from ckanext.berlintheme.diff.griddiff import GridDiff

LOG = logging.getLogger(__name__)

def activity_diff(context, data_dict):
    '''Returns a diff of the activity, compared to the previous version of the
    object

    :param id: the id of the activity
    :type id: string
    :param object_type: 'package', 'user', 'group' or 'organization'
    :type object_type: string
    :param diff_type: 'unified', 'context', 'html'
    :type diff_type: string
    '''
    import difflib

    model = context['model']
    activity_id = ckanget._get_or_bust(data_dict, 'id')
    object_type = ckanget._get_or_bust(data_dict, 'object_type')
    diff_type = data_dict.get('diff_type', 'unified')

    ckanget._check_access(u'activity_diff', context, data_dict)

    activity = model.Session.query(model.Activity).get(activity_id)
    if activity is None:
        raise NotFound
    prev_activity = model.Session.query(model.Activity) \
        .filter_by(object_id=activity.object_id) \
        .filter(model.Activity.timestamp < activity.timestamp) \
        .order_by(model.Activity.timestamp.desc()) \
        .first()
    if prev_activity is None:
        raise NotFound('Previous activity for this object not found')
    activity_objs = [prev_activity, activity]
    try:
        objs = [activity_obj.data[object_type]
                for activity_obj in activity_objs]
    except KeyError:
        raise NotFound('Could not find object in the activity data')
    # convert each object dict to 'pprint'-style
    # and split into lines to suit difflib
    obj_lines = [json.dumps(obj, indent=2, sort_keys=True).split('\n')
                 for obj in objs]

    # do the diff
    if diff_type == 'unified':
        diff_generator = difflib.unified_diff(*obj_lines)
        diff = '\n'.join(line for line in diff_generator)
    elif diff_type == 'context':
        diff_generator = difflib.context_diff(*obj_lines)
        diff = '\n'.join(line for line in diff_generator)
    elif diff_type == 'html':
        diff = GridDiff().make_grid(obj_lines[0], obj_lines[1])
    else:
        raise ValidationError('diff_type not recognized')

    activities = [model_dictize.activity_dictize(activity_obj, context,
                                                 include_data=True)
                  for activity_obj in activity_objs]

    return {
        'diff': diff,
        'activities': activities,
        }

@ckan.logic.side_effect_free
def status_show(context, data_dict):
    '''Implementation of ckan.logic.action.get.status_show

    Replaces the plain list of extensions with a list of dicts that contain
    the extension's name and version number, based on a __version__ attribute.

    :rtype: dictionary

    '''

    def build_ext_dict(ext_name: str)->dict:
        import traceback
        version = "unknown"
        try:
            meta = md.metadata(f'ckanext-{ext_name}')
            version = md.version(f'ckanext-{ext_name}')
        except ModuleNotFoundError as e:
            LOG.error(traceback.format_exc())
            return { "version": version, "error": e.__class__.__name__ }
        url = meta['Home-page']
        return { 'version': version, 'url': url }

    status_dict = ckanget.status_show(context, data_dict)
    extensions = status_dict['extensions']
    extensions = { ext_name: build_ext_dict(ext_name) for ext_name in extensions }
    status_dict['extensions'] = extensions
    return status_dict
