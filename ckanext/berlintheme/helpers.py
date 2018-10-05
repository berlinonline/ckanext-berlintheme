# coding: utf-8

import logging
import ckan.logic as logic
import ckan.model as model
from ckan.common import c
from ckanext.berlin_dataset_schema.schema import Schema

log = logging.getLogger(__name__)
get_action = logic.get_action

def required(attribute):
    return Schema().required(attribute)

def classes_for_attribute(attribute, classes, as_string=False):
    if required(attribute):
        classes.append('datasetform-required')
    if as_string:
        classes = " ".join(classes)
    return classes

def dataset_type_mapping():
    return {
        'datensatz': 'Datensatz',
        'dokument': 'Dokument',
        'app': 'Anwendung'
    }

def group_mapping():
    context = {
        'model': model,
        'session': model.Session,
        'user': c.user,
        'for_view': True,
        'auth_user_obj': c.userobj,
        'use_cache': False
    }
    context['is_member'] = True

    users_groups = get_action('group_list_authz')(context, {})
    mapping = [ { "text": group['display_name'], "value": group['name']} for group in users_groups ]
    return mapping

def geo_coverage_select_options():
    return [
        {u'id': u'Keine', u'label': u'Keine'},
        {u'id': u'Adlershof', u'label': u'Adlershof'},
        {u'id': u'Alt-Hohenschönhausen', u'label': u'Alt-Hohenschönhausen'},
        {u'id': u'Alt-Treptow', u'label': u'Alt-Treptow'},
        {u'id': u'Altglienicke', u'label': u'Altglienicke'},
        {u'id': u'Baumschulenweg', u'label': u'Baumschulenweg'},
        {u'id': u'Berlin', u'label': u'Berlin'},
        {u'id': u'Biesdorf', u'label': u'Biesdorf'},
        {u'id': u'Blankenburg', u'label': u'Blankenburg'},
        {u'id': u'Blankenfelde', u'label': u'Blankenfelde'},
        {u'id': u'Bohnsdorf', u'label': u'Bohnsdorf'},
        {u'id': u'Britz', u'label': u'Britz'},
        {u'id': u'Buch', u'label': u'Buch'},
        {u'id': u'Buckow', u'label': u'Buckow'},
        {u'id': u'Charlottenburg', u'label': u'Charlottenburg'},
        {u'id': u'Charlottenburg-Nord', u'label': u'Charlottenburg-Nord'},
        {u'id': u'Charlottenburg-Wilmersdorf', u'label': u'Charlottenburg-Wilmersdorf'},
        {u'id': u'Dahlem', u'label': u'Dahlem'},
        {u'id': u'Deutschland', u'label': u'Deutschland'},
        {u'id': u'Friedenau', u'label': u'Friedenau'},
        {u'id': u'Friedrichsfelde', u'label': u'Friedrichsfelde'},
        {u'id': u'Friedrichshagen', u'label': u'Friedrichshagen'},
        {u'id': u'Friedrichshain', u'label': u'Friedrichshain'},
        {u'id': u'Friedrichshain-Kreuzberg', u'label': u'Friedrichshain-Kreuzberg'},
        {u'id': u'Frohnau', u'label': u'Frohnau'},
        {u'id': u'Gatow', u'label': u'Gatow'},
        {u'id': u'Gesundbrunnen', u'label': u'Gesundbrunnen'},
        {u'id': u'Gropiusstadt', u'label': u'Gropiusstadt'},
        {u'id': u'Grunewald', u'label': u'Grunewald'},
        {u'id': u'Grünau', u'label': u'Grünau'},
        {u'id': u'Hakenfelde', u'label': u'Hakenfelde'},
        {u'id': u'Halensee', u'label': u'Halensee'},
        {u'id': u'Hansaviertel', u'label': u'Hansaviertel'},
        {u'id': u'Haselhorst', u'label': u'Haselhorst'},
        {u'id': u'Heiligensee', u'label': u'Heiligensee'},
        {u'id': u'Heinersdorf', u'label': u'Heinersdorf'},
        {u'id': u'Hellersdorf', u'label': u'Hellersdorf'},
        {u'id': u'Hermsdorf', u'label': u'Hermsdorf'},
        {u'id': u'Hohenschönhausen', u'label': u'Hohenschönhausen'},
        {u'id': u'Johannisthal', u'label': u'Johannisthal'},
        {u'id': u'Karlshorst', u'label': u'Karlshorst'},
        {u'id': u'Karow', u'label': u'Karow'},
        {u'id': u'Kaulsdorf', u'label': u'Kaulsdorf'},
        {u'id': u'Kladow', u'label': u'Kladow'},
        {u'id': u'Kreuzberg', u'label': u'Kreuzberg'},
        {u'id': u'Lichtenberg', u'label': u'Lichtenberg'},
        {u'id': u'Lichtenrade', u'label': u'Lichtenrade'},
        {u'id': u'Lichterfelde', u'label': u'Lichterfelde'},
        {u'id': u'Lübars', u'label': u'Lübars'},
        {u'id': u'Mahlsdorf', u'label': u'Mahlsdorf'},
        {u'id': u'Malchow', u'label': u'Malchow'},
        {u'id': u'Mariendorf', u'label': u'Mariendorf'},
        {u'id': u'Marienfelde', u'label': u'Marienfelde'},
        {u'id': u'Marzahn', u'label': u'Marzahn'},
        {u'id': u'Marzahn-Hellersdorf', u'label': u'Marzahn-Hellersdorf'},
        {u'id': u'Mitte', u'label': u'Mitte'},
        {u'id': u'Moabit', u'label': u'Moabit'},
        {u'id': u'Märkisches Viertel', u'label': u'Märkisches Viertel'},
        {u'id': u'Müggelheim', u'label': u'Müggelheim'},
        {u'id': u'Neu-Hohenschönhausen', u'label': u'Neu-Hohenschönhausen'},
        {u'id': u'Neukölln', u'label': u'Neukölln'},
        {u'id': u'Niederschöneweide', u'label': u'Niederschöneweide'},
        {u'id': u'Niederschönhausen', u'label': u'Niederschönhausen'},
        {u'id': u'Nikolassee', u'label': u'Nikolassee'},
        {u'id': u'Oberschöneweide', u'label': u'Oberschöneweide'},
        {u'id': u'Pankow', u'label': u'Pankow'},
        {u'id': u'Plänterwald', u'label': u'Plänterwald'},
        {u'id': u'Prenzlauer Berg', u'label': u'Prenzlauer Berg'},
        {u'id': u'Rahnsdorf', u'label': u'Rahnsdorf'},
        {u'id': u'Reinickendorf', u'label': u'Reinickendorf'},
        {u'id': u'Schmöckwitz', u'label': u'Schmöckwitz'},
        {u'id': u'Schöneberg', u'label': u'Schöneberg'},
        {u'id': u'Siemensstadt', u'label': u'Siemensstadt'},
        {u'id': u'Spandau', u'label': u'Spandau'},
        {u'id': u'Staaken', u'label': u'Staaken'},
        {u'id': u'Stadtrandsiedlung Malchow', u'label': u'Stadtrandsiedlung Malchow'},
        {u'id': u'Steglitz', u'label': u'Steglitz'},
        {u'id': u'Steglitz-Zehlendorf', u'label': u'Steglitz-Zehlendorf'},
        {u'id': u'Tegel', u'label': u'Tegel'},
        {u'id': u'Tempelhof', u'label': u'Tempelhof'},
        {u'id': u'Tempelhof-Schöneberg', u'label': u'Tempelhof-Schöneberg'},
        {u'id': u'Tiergarten', u'label': u'Tiergarten'},
        {u'id': u'Treptow-Köpenick', u'label': u'Treptow-Köpenick'},
        {u'id': u'Waidmannslust', u'label': u'Waidmannslust'},
        {u'id': u'Wannsee', u'label': u'Wannsee'},
        {u'id': u'Wartenberg', u'label': u'Wartenberg'},
        {u'id': u'Wedding', u'label': u'Wedding'},
        {u'id': u'Weißensee', u'label': u'Weißensee'},
        {u'id': u'Westend', u'label': u'Westend'},
        {u'id': u'Wilhelmsruh', u'label': u'Wilhelmsruh'},
        {u'id': u'Wilhelmstadt', u'label': u'Wilhelmstadt'},
        {u'id': u'Wilmersdorf', u'label': u'Wilmersdorf'},
        {u'id': u'Wittenau', u'label': u'Wittenau'},
        {u'id': u'Zehlendorf', u'label': u'Zehlendorf'},
    ]


def type_mapping_select_options():
    options = []
    for machine, human in dataset_type_mapping().items():
        options.append({'text': human, 'value': machine})
    return options

def group_select_options():
    options = [ { 
        'text': u'Bitte eine Kategorie auswählen' ,
        'value': u'empty'
    }]
    options = options + group_mapping()
    return options

# eventually, these values should come from a JSON API
# ids should be URIs, not just the label string
def temporal_granularity_select_options():
    return [
        {u'id': u'Keine', u'label': u'Keine'},
        {u'id': u'5 Jahre', u'label': u'5 Jahre'},
        {u'id': u'Jahr', u'label': u'Jahr'},
        {u'id': u'Quartal', u'label': u'Quartal'},
        {u'id': u'Monat', u'label': u'Monat'},
        {u'id': u'Woche', u'label': u'Woche'},
        {u'id': u'Tag', u'label': u'Tag'},
        {u'id': u'Stunde', u'label': u'Stunde'},
        {u'id': u'Minute', u'label': u'Minute'},
        {u'id': u'Sekunde', u'label': u'Sekunde'},
    ]


# eventually, these values should come from a JSON API
# ids should be URIs, not just the label string
def geo_granularity_select_options():
    return [
        {u'id': u'Keine', u'label': u'Keine'},
        {u'id': u'Deutschland', u'label': u'Deutschland'},
        {u'id': u'Berlin', u'label': u'Berlin'},
        {u'id': u'Bezirk', u'label': u'Bezirk'},
        {u'id': u'Ortsteil', u'label': u'Ortsteil'},
        {u'id': u'Prognoseraum', u'label': u'Prognoseraum'},
        {u'id': u'Bezirksregion', u'label': u'Bezirksregion'},
        {u'id': u'Planungsraum', u'label': u'Planungsraum'},
        {u'id': u'Block', u'label': u'Block'},
        {u'id': u'Einschulbereich', u'label': u'Einschulbereich'},
        {u'id': u'Kontaktbereich', u'label': u'Kontaktbereich'},
        {u'id': u'PLZ', u'label': u'PLZ'},
        {u'id': u'Stimmbezirk', u'label': u'Stimmbezirk'},
        {u'id': u'Quartiersmanagement', u'label': u'Quartiersmanagement'},
        {u'id': u'Wohnanlage', u'label': u'Wohnanlage'},
        {u'id': u'Wahlkreis', u'label': u'Wahlkreis'},
        {u'id': u'Adresse', u'label': u'Adresse'},
        {u'id': u'GPS-Koordinaten', u'label': u'GPS-Koordinaten'},
    ]


def state_mapping():
    return {
        'active': u'veröffentlicht',
        'deleted': u'gelöscht'
    }


def organizations_for_user(user, permission='create_dataset'):
    '''Return a list of organizations that the given user has the specified
    permission for.
    '''
    context = {'user': user}
    data_dict = {'permission': permission}
    return logic.get_action('organization_list_for_user')(context, data_dict)


def is_sysadmin(user_name):
    user = model.User.get(unicode(user_name))
    return user.sysadmin

def first_group_name(data_dict):
    groups = data_dict.get('groups', [])
    if len(groups) > 0:
        return groups[0].get('name', None)
    return None