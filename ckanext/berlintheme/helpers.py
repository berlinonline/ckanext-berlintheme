# coding: utf-8

import logging

from ckan.common import c, config
from ckan.lib.helpers import link_to
import ckan.logic as logic
import ckan.model as model
import ckan.plugins.toolkit as toolkit

from ckanext.berlin_dataset_schema.schema import Schema

log = logging.getLogger(__name__)
get_action = logic.get_action

def required(attribute):
    return Schema().required(attribute)

def dataset_type_mapping():
    return {
        'datensatz': 'Datensatz',
        'dokument': 'Dokument'
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
        {u'id': u'Hausnummer', u'label': u'Hausnummer'},
        {u'id': u'GPS-Koordinaten', u'label': u'GPS-Koordinaten'},
    ]

def sample_record_select_options():
    return [
        {'id': 'Stadtplan/Stadtmodell3d', 'label': "Stadtplan - Stadtmodell 3D"},
        {'id': 'Stadtplan/stadtplaene', 'label': "Stadtplan - Stadtpläne"},
        {'id': 'abfallwirtschaft/abfallkalender', 'label': "Abfallwirtschaft - Abfallkalender"},
        {'id': 'abfallwirtschaft/abfallmengen', 'label': "Abfallwirtschaft - Abfallmengen"},
        {'id': 'abfallwirtschaft/abgabestellen', 'label': "Abfallwirtschaft - Abgabestellen"},
        {'id': 'abfallwirtschaft/beteiligungen', 'label': "Abfallwirtschaft - Beteiligungen"},
        {'id': 'abfallwirtschaft/betriebe', 'label': "Abfallwirtschaft - Betriebe"},
        {'id': 'abfallwirtschaft/container', 'label': "Abfallwirtschaft - Container"},
        {'id': 'abfallwirtschaft/entwaesserung', 'label': "Abfallwirtschaft - Entwässerung"},
        {'id': 'abfallwirtschaft/gremien', 'label': "Abfallwirtschaft - Gremien"},
        {'id': 'abfallwirtschaft/muellabfuhr', 'label': "Abfallwirtschaft - Müllabfuhr"},
        {'id': 'abfallwirtschaft/muellgebuehren', 'label': "Abfallwirtschaft - Müllgebühren"},
        {'id': 'bau/baufertigstellungen', 'label': "Bau - Baufertigstellungen"},
        {'id': 'bau/baugenehmigungen', 'label': "Bau - Baugenehmigungen"},
        {'id': 'bau/bauprojekte', 'label': "Bau - Bauprojekte"},
        {'id': 'bau/gebaeude', 'label': "Bau - Gebäude"},
        {'id': 'bau/grundstueckbewertung', 'label': "Bau - Grundstückbewertung"},
        {'id': 'behoerden/einrichtungen', 'label': "Behörden - Einrichtungen"},
        {'id': 'bevoelkerung/arbeit', 'label': "Bevölkerung - Arbeit"},
        {'id': 'bevoelkerung/bedarfsgemeinschaften', 'label': "Bevölkerung - Bedarfsgemeinschaften"},
        {'id': 'bevoelkerung/demografie', 'label': "Bevölkerung - Demografie"},
        {'id': 'bevoelkerung/einwohnerzahl', 'label': "Bevölkerung - Einwohnerzahl"},
        {'id': 'bevoelkerung/fluechtlingszahlen', 'label': "Bevölkerung - Flüchtlingszahlen"},
        {'id': 'bevoelkerung/geburtenUndSterbefaelle', 'label': "Bevölkerung - Geburten und Sterbefälle"},
        {'id': 'bevoelkerung/integration', 'label': "Bevölkerung - Integration"},
        {'id': 'bevoelkerung/menschenMitBehinderung', 'label': "Bevölkerung - Menschen mit Behinderung"},
        {'id': 'bevoelkerung/migrationshintergrund', 'label': "Bevölkerung - Migrationshintergrund"},
        {'id': 'bevoelkerung/religionszugehoerigkeit', 'label': "Bevölkerung - Religionszugehörigkeit"},
        {'id': 'bevoelkerung/staatsangehoerigkeit', 'label': "Bevölkerung - Staatsangehörigkeit"},
        {'id': 'bevoelkerung/vornamen', 'label': "Bevölkerung - Vornamen"},
        {'id': 'bevoelkerung/wohnen', 'label': "Bevölkerung - Wohnen"},
        {'id': 'bibliotheken/ausleihen', 'label': "Bibliotheken - Ausleihen"},
        {'id': 'bibliotheken/bestaende', 'label': "Bibliotheken - Bestände"},
        {'id': 'bibliotheken/besucherzahlen', 'label': "Bibliotheken - Besucherzahlen"},
        {'id': 'bibliotheken/budget', 'label': "Bibliotheken - Budget"},
        {'id': 'bibliotheken/einrichtungen', 'label': "Bibliotheken - Einrichtungen"},
        {'id': 'bibliotheken/kennzahlen', 'label': "Bibliotheken - Kennzahlen"},
        {'id': 'bildungstraeger/einrichtungen', 'label': "Bildungsträger - Einrichtungen"},
        {'id': 'buergerbeteiligung/buergerentscheid', 'label': "Bürgerbeteiligung - Bürgerentscheid"},
        {'id': 'buergerbeteiligung/buergerhaushalt', 'label': "Bürgerbeteiligung - Bürgerhaushalt"},
        {'id': 'buergerbeteiligung/information', 'label': "Bürgerbeteiligung - Information"},
        {'id': 'buergerbeteiligung/umfrage', 'label': "Bürgerbeteiligung - Umfrage"},
        {'id': 'buergerservice/anliegenmanagement', 'label': "Bürgerservice - Anliegenmanagement"},
        {'id': 'buergerservice/produkte', 'label': "Bürgerservice - Produkte"},
        {'id': 'buergerservice/telefonverzeichnis', 'label': "Bürgerservice - Telefonverzeichnis"},
        {'id': 'buergerservice/termine', 'label': "Bürgerservice - Termine"},
        {'id': 'buergerservice/wartezeiten', 'label': "Bürgerservice - Wartezeiten"},
        {'id': 'energiewirtschaft/energieberichte', 'label': "Energiewirtschaft - Energieberichte"},
        {'id': 'energiewirtschaft/heizung', 'label': "Energiewirtschaft - Heizung"},
        {'id': 'energiewirtschaft/solar', 'label': "Energiewirtschaft - Solar"},
        {'id': 'energiewirtschaft/strom', 'label': "Energiewirtschaft - Strom"},
        {'id': 'energiewirtschaft/wasser', 'label': "Energiewirtschaft - Wasser"},
        {'id': 'externeInfrastruktur/coworkingSpaces', 'label': "Externe Infrastruktur - Coworking Spaces"},
        {'id': 'externeInfrastruktur/einkaufsfuehrer', 'label': "Externe Infrastruktur - Einkaufsführer"},
        {'id': 'externeInfrastruktur/einzelhandel', 'label': "Externe Infrastruktur - Einzelhandel"},
        {'id': 'externeInfrastruktur/kirchenKappellenUndKloester', 'label': "Externe Infrastruktur - Kirchen, Kapellen und Klöster"},
        {'id': 'externeInfrastruktur/maerkte', 'label': "Externe Infrastruktur - Märkte"},
        {'id': 'externeInfrastruktur/oeffnungszeiten', 'label': "Externe Infrastruktur - Öffnungszeiten"},
        {'id': 'externeInfrastruktur/polizei', 'label': "Externe Infrastruktur - Polizei"},
        {'id': 'externeInfrastruktur/postfilialen', 'label': "Externe Infrastruktur - Postfilialen"},
        {'id': 'externeInfrastruktur/weihnachtsmaerkte', 'label': "Externe Infrastruktur - Weihnachtsmärkte"},
        {'id': 'externeInfrastruktur/wochenmaerkte', 'label': "Externe Infrastruktur - Wochenmärkte"},
        {'id': 'feuerwehr/einrichtungen', 'label': "Feuerwehr - Einrichtungen"},
        {'id': 'feuerwehr/einsaetze', 'label': "Feuerwehr - Einsätze"},
        {'id': 'feuerwehr/kennzahlen', 'label': "Feuerwehr - Kennzahlen"},
        {'id': 'freizeit/baeder', 'label': "Freizeit - Bäder"},
        {'id': 'freizeit/einrichtungen', 'label': "Freizeit - Einrichtungen"},
        {'id': 'freizeit/ferienangebot', 'label': "Freizeit - Ferienangebot"},
        {'id': 'freizeit/grillplaetze', 'label': "Freizeit - Grillplätze"},
        {'id': 'freizeit/sitzgelegenheiten', 'label': "Freizeit - Sitzgelegenheiten"},
        {'id': 'friedhoefe/ehrengraeber', 'label': "Friedhöfe - Ehrengräber"},
        {'id': 'friedhoefe/einrichtungen', 'label': "Friedhöfe - Einrichtungen"},
        {'id': 'friedhoefe/grabstaetten', 'label': "Friedhöfe - Grabstätten"},
        {'id': 'fuhrpark/kfzBestand', 'label': "Fuhrpark - KFZ-Bestand"},
        {'id': 'geschichte/archivbestand', 'label': "Geschichte - Archivbestand"},
        {'id': 'geschichte/entschaedigungen', 'label': "Geschichte - Entschädigungen"},
        {'id': 'geschichte/historischeLuftaufnahmen', 'label': "Geschichte - Historische Luftaufnahmen"},
        {'id': 'geschichte/information', 'label': "Geschichte - Information"},
        {'id': 'geschichte/personalverzeichnisHistorisch', 'label': "Geschichte - Personalverzeichnis historisch"},
        {'id': 'gesundheitseinrichtungen/apotheken', 'label': "Gesundheitseinrichtungen - Apotheken"},
        {'id': 'gesundheitseinrichtungen/baeder', 'label': "Gesundheitseinrichtungen - Bäder"},
        {'id': 'gesundheitseinrichtungen/drogenhilfe', 'label': "Gesundheitseinrichtungen - Drogenhilfe"},
        {'id': 'gesundheitseinrichtungen/hebammen', 'label': "Gesundheitseinrichtungen - Hebammen"},
        {'id': 'gesundheitseinrichtungen/krankenhaeuser', 'label': "Gesundheitseinrichtungen - Krankenhäuser"},
        {'id': 'gesundheitseinrichtungen/pflege', 'label': "Gesundheitseinrichtungen - Pflege"},
        {'id': 'gewaesser/pegelstaende', 'label': "Gewässer - Pegelstände"},
        {'id': 'gewaesser/wasserflaechen', 'label': "Gewässer - Wasserflächen"},
        {'id': 'gruenflaechen/ausgleichsflaechen', 'label': "Grünflächen - Ausgleichsflächen"},
        {'id': 'gruenflaechen/baumbestandBaumkataster', 'label': "Grünflächen - Baumbestand/Baumkataster"},
        {'id': 'gruenflaechen/baumfaellungen', 'label': "Grünflächen - Baumfällungen"},
        {'id': 'gruenflaechen/biotopflaechen', 'label': "Grünflächen - Biotopflächen"},
        {'id': 'gruenflaechen/blumenampeln', 'label': "Grünflächen - Blumenampeln"},
        {'id': 'gruenflaechen/brunnen', 'label': "Grünflächen - Brunnen"},
        {'id': 'gruenflaechen/gruenflaechenGruenflaechenkataster', 'label': "Grünflächen - Grünflächen/Grünflächenkataster"},
        {'id': 'gruenflaechen/hundekottueten', 'label': "Grünflächen - Hundekottüten"},
        {'id': 'gruenflaechen/hundewiesen', 'label': "Grünflächen - Hundewiesen"},
        {'id': 'gruenflaechen/jagdbezirke', 'label': "Grünflächen - Jagdbezirke"},
        {'id': 'gruenflaechen/kleingaerten', 'label': "Grünflächen - Kleingärten"},
        {'id': 'gruenflaechen/naturschutz', 'label': "Grünflächen - Naturschutz"},
        {'id': 'gruenflaechen/parkanlagen', 'label': "Grünflächen - Parkanlagen"},
        {'id': 'gruenflaechen/urbanGardening', 'label': "Grünflächen - Urban Gardening"},
        {'id': 'gruenflaechen/waldflaechen', 'label': "Grünflächen - Waldflächen"},
        {'id': 'haushalt/ausserplanmaessigeAufwendungen', 'label': "Haushalt - Außerplanmäßige Aufwendungen"},
        {'id': 'haushalt/controlling', 'label': "Haushalt - Controlling"},
        {'id': 'haushalt/eckdaten', 'label': "Haushalt - Eckdaten"},
        {'id': 'haushalt/einzeldarstellungen', 'label': "Haushalt - Einzeldarstellungen"},
        {'id': 'haushalt/ergebnisplan', 'label': "Haushalt - Ergebnisplan"},
        {'id': 'haushalt/finanzplan', 'label': "Haushalt - Finanzplan"},
        {'id': 'haushalt/foerderungen', 'label': "Haushalt - Förderungen"},
        {'id': 'haushalt/haushaltskonsolidierung', 'label': "Haushalt - Haushaltskonsolidierung"},
        {'id': 'haushalt/haushaltsplan', 'label': "Haushalt - Haushaltsplan"},
        {'id': 'haushalt/jahresabschluss', 'label': "Haushalt - Jahresabschluss"},
        {'id': 'haushalt/metadaten', 'label': "Haushalt - Metadaten"},
        {'id': 'haushalt/produktbereichsummen', 'label': "Haushalt - Produktbereichssummen"},
        {'id': 'haushalt/produktgruppen', 'label': "Haushalt - Produktgruppen"},
        {'id': 'haushalt/produktplaene', 'label': "Haushalt - Produktpläne"},
        {'id': 'haushalt/satzung', 'label': "Haushalt - Satzung"},
        {'id': 'haushalt/sicherungskonzept', 'label': "Haushalt - Sicherungskonzept"},
        {'id': 'haushalt/sponsoring', 'label': "Haushalt - Sponsoring"},
        {'id': 'haushalt/zuwendungenPolitischeGremien', 'label': "Haushalt - Zuwendungen Politische Gremien"},
        {'id': 'hochschulen/gebaeude', 'label': "Hochschulen - Gebäude"},
        {'id': 'hochschulen/studierendenzahlen', 'label': "Hochschulen - Studierendenzahlen"},
        {'id': 'individualverkehr/baustellen', 'label': "Individualverkehr - Baustellen"},
        {'id': 'individualverkehr/bussgelder', 'label': "Individualverkehr - Bußgelder"},
        {'id': 'individualverkehr/carsharing', 'label': "Individualverkehr - Carsharing"},
        {'id': 'individualverkehr/fahrzeugzulassungen', 'label': "Individualverkehr - Fahrzeugzulassungen"},
        {'id': 'individualverkehr/kennzahlen', 'label': "Individualverkehr - Kennzahlen"},
        {'id': 'individualverkehr/kfzBestand', 'label': "Individualverkehr - KFZ-Bestand"},
        {'id': 'individualverkehr/laerm', 'label': "Individualverkehr - Lärm"},
        {'id': 'individualverkehr/messstellen', 'label': "Individualverkehr - Messstellen"},
        {'id': 'individualverkehr/schwerlastverkehr', 'label': "Individualverkehr - Schwerlastverkehr"},
        {'id': 'individualverkehr/sondernutzungen', 'label': "Individualverkehr - Sondernutzungen"},
        {'id': 'individualverkehr/strassenverkehr', 'label': "Individualverkehr - Straßenverkehr"},
        {'id': 'individualverkehr/taxis', 'label': "Individualverkehr - Taxis"},
        {'id': 'individualverkehr/unfaelle', 'label': "Individualverkehr - Unfälle"},
        {'id': 'infrastruktur/adressen', 'label': "Infrastruktur - Adressen"},
        {'id': 'infrastruktur/ampelanlagen', 'label': "Infrastruktur - Ampelanlagen"},
        {'id': 'infrastruktur/autobahnbindung', 'label': "Infrastruktur - Autobahnanbindung"},
        {'id': 'infrastruktur/baustellen', 'label': "Infrastruktur - Baustellen"},
        {'id': 'infrastruktur/beleuchtungen', 'label': "Infrastruktur - Beleuchtung"},
        {'id': 'infrastruktur/bruecken', 'label': "Infrastruktur - Brücken"},
        {'id': 'infrastruktur/elektrotankstellen', 'label': "Infrastruktur - Elektrotankstellen"},
        {'id': 'infrastruktur/fahrradstrassen', 'label': "Infrastruktur - Fahrradstraßen"},
        {'id': 'infrastruktur/flughaefen', 'label': "Infrastruktur - Flughäfen"},
        {'id': 'infrastruktur/fussgaengerzonen', 'label': "Infrastruktur - Fußgängerzonen"},
        {'id': 'infrastruktur/laufstrecken', 'label': "Infrastruktur - Laufstrecken"},
        {'id': 'infrastruktur/oeffentlicheToiletten', 'label': "Infrastruktur - Öffentliche Toiletten"},
        {'id': 'infrastruktur/parkplaetze', 'label': "Infrastruktur - Parkplätze"},
        {'id': 'infrastruktur/schiffsanlegestellen', 'label': "Infrastruktur - Schiffsanlegestellen"},
        {'id': 'infrastruktur/strassen', 'label': "Infrastruktur - Straßen"},
        {'id': 'infrastruktur/strassenreinigung', 'label': "Infrastruktur - Straßenreinigung"},
        {'id': 'infrastruktur/tankstellen', 'label': "Infrastruktur - Tankstellen"},
        {'id': 'infrastruktur/wlanUndMobilfunk', 'label': "Infrastruktur - WLAN und Mobilfunk"},
        {'id': 'jugend/einrichtungen', 'label': "Jugend - Einrichtungen"},
        {'id': 'justiz/einrichtungen', 'label': "Justiz - Einrichtungen"},
        {'id': 'justiz/gesetzestexte', 'label': "Justiz - Gesetzestexte"},
        {'id': 'kindertageseinrichtungen/betreuungsplaetze', 'label': "Kindertageseinrichtungen - Betreuungsplätze"},
        {'id': 'kindertageseinrichtungen/kindertagesstaetten', 'label': "Kindertageseinrichtungen - Kindertagestätten"},
        {'id': 'kultur/besucherzahlen', 'label': "Kultur - Besucherzahlen"},
        {'id': 'kultur/denkmaeler', 'label': "Kultur - Denkmäler"},
        {'id': 'kultur/foerderungen', 'label': "Kultur - Förderungen"},
        {'id': 'kultur/information', 'label': "Kultur - Information"},
        {'id': 'kultur/kunstwerke', 'label': "Kultur - Kunstwerke"},
        {'id': 'kultur/lehrUndWanderpfade', 'label': "Kultur - Lehr- und Wanderpfade"},
        {'id': 'kultur/veranstaltungen', 'label': "Kultur - Veranstaltungen"},
        {'id': 'liegenschaften/gebaeude', 'label': "Liegenschaften - Gebäude"},
        {'id': 'liegenschaften/grundstuecke', 'label': "Liegenschaften - Grundstücke"},
        {'id': 'liegenschaften/jahresberichte', 'label': "Liegenschaften - Jahresberichte"},
        {'id': 'liegenschaften/satzungen', 'label': "Liegenschaften - Satzungen"},
        {'id': 'museen/besucherzahlen', 'label': "Museen - Besucherzahlen"},
        {'id': 'museen/einrichtungen', 'label': "Museen - Einrichtungen"},
        {'id': 'musikschulen/jahresrechnung', 'label': "Musikschulen - Jahresrechnung"},
        {'id': 'musikschulen/teilnehmer', 'label': "Musikschulen - Teilnehmer"},
        {'id': 'musikschulen/unterrichtsangebot', 'label': "Musikschulen - Unterrichtsangebot"},
        {'id': 'oeffentlicheWirtschaft/ausschreibungenVergaben', 'label': "Öffentliche Wirtschaft - Ausschreibungen Vergaben"},
        {'id': 'oeffentlicheWirtschaft/beteiligungen', 'label': "Öffentliche Wirtschaft - Beteiligungen"},
        {'id': 'oeffentlichkeitsarbeit/amtsblatt', 'label': "Öffentlichkeitsarbeit - Amtsblatt"},
        {'id': 'oeffentlichkeitsarbeit/ehrenbuerrger', 'label': "Öffentlichkeitsarbeit - Ehrenbürger"},
        {'id': 'oeffentlichkeitsarbeit/fotos', 'label': "Öffentlichkeitsarbeit - Fotos"},
        {'id': 'oeffentlichkeitsarbeit/information', 'label': "Öffentlichkeitsarbeit - Information"},
        {'id': 'oeffentlichkeitsarbeit/pressemitteilungen', 'label': "Öffentlichkeitsarbeit - Pressemitteilungen"},
        {'id': 'oepnv/aufzuegeUndRolltreppen', 'label': "ÖPNV - Aufzüge und Rolltreppen"},
        {'id': 'oepnv/befragungen', 'label': "ÖPNV - Befragung"},
        {'id': 'oepnv/fahrgastzahlen', 'label': "ÖPNV - Fahrgastzahlen"},
        {'id': 'oepnv/haltestellen', 'label': "ÖPNV - Haltestellen"},
        {'id': 'oepnv/liniennetz', 'label': "ÖPNV - Liniennetz"},
        {'id': 'oepnv/sollfahrdaten', 'label': "ÖPNV - Sollfahrdaten"},
        {'id': 'oepnv/verkehrsnetz', 'label': "ÖPNV - Verkehrsnetz"},
        {'id': 'oepnv/vertriebsstellen', 'label': "ÖPNV - Vertriebsstellen"},
        {'id': 'openData/information', 'label': "Open Data - Information"},
        {'id': 'openData/wunschlisten', 'label': "Open Data - Wunschlisten"},
        {'id': 'openData/zugriffe', 'label': "Open Data - Zugriffe"},
        {'id': 'personal/stellenplan', 'label': "Personal - Stellenplan"},
        {'id': 'politischeVertretung/buergermeister', 'label': "Politische Vertretung - Bürgermeister"},
        {'id': 'politischeVertretung/gremien', 'label': "Politische Vertretung - Gremien"},
        {'id': 'politischeVertretung/mandatstraeger', 'label': "Politische Vertretung - Mandatsträger"},
        {'id': 'radverkehr/buergerbeteiligung', 'label': "Radverkehr - Bürgerbeteiligung"},
        {'id': 'radverkehr/fahrraeder', 'label': "Radverkehr - Fahrräder"},
        {'id': 'radverkehr/foerderungen', 'label': "Radverkehr - Förderungen"},
        {'id': 'radverkehr/ladestationen', 'label': "Radverkehr - Ladestationen"},
        {'id': 'radverkehr/messstellen', 'label': "Radverkehr - Messstellen"},
        {'id': 'radverkehr/radrouten', 'label': "Radverkehr - Radrouten"},
        {'id': 'radverkehr/stellplaetze', 'label': "Radverkehr - Stellplätze"},
        {'id': 'raumordnung/adressen', 'label': "Raumordnung - Adressen"},
        {'id': 'raumordnung/baublockgrenzen', 'label': "Raumordnung - Baublockgrenzen"},
        {'id': 'raumordnung/bebauungsplaene', 'label': "Raumordnung - Bebauungspläne"},
        {'id': 'raumordnung/bloecke', 'label': "Raumordnung - Blöcke"},
        {'id': 'raumordnung/flaechennutzungen', 'label': "Raumordnung - Flächennutzungen"},
        {'id': 'raumordnung/hausnummern', 'label': "Raumordnung - Hausnummern"},
        {'id': 'raumordnung/liegenschaftskataster', 'label': "Raumordnung - Liegenschaftskataster"},
        {'id': 'raumordnung/orthofotos', 'label': "Raumordnung - Orthofotos"},
        {'id': 'raumordnung/ortsteile', 'label': "Raumordnung - Ortsteile"},
        {'id': 'raumordnung/postleitzahlengebiete', 'label': "Raumordnung - Postleitzahlengebiete"},
        {'id': 'raumordnung/sozialraeume', 'label': "Raumordnung - Sozialräume"},
        {'id': 'raumordnung/stadtgebiet', 'label': "Raumordnung - Stadtgebiet"},
        {'id': 'rettungsdienst/defibrillatoren', 'label': "Rettungsdienst - Defibrillatoren"},
        {'id': 'rettungsdienst/einsaetze', 'label': "Rettungsdienst - Einsätze"},
        {'id': 'rettungsdienst/reanimationen', 'label': "Rettungsdienst - Reanimationen"},
        {'id': 'rettungsdienst/rettungspunkt', 'label': "Rettungsdienst - Rettungspunkt"},
        {'id': 'schulen/einrichtungen', 'label': "Schulen - Einrichtungen"},
        {'id': 'schulen/internetanbindung', 'label': "Schulen - Internetanbindung"},
        {'id': 'schulen/schuelerzahlen', 'label': "Schulen - Schülerzahlen"},
        {'id': 'schulen/schulangebot', 'label': "Schulen - Schulangebot"},
        {'id': 'schulen/schuleingangsuntersuchungen', 'label': "Schulen - Schuleingangsunteruchungen"},
        {'id': 'schulen/schulentwicklungsplan', 'label': "Schulen - Schulentwicklungsplan"},
        {'id': 'schulen/wunschschule', 'label': "Schulen - Wunschschule"},
        {'id': 'senioren/einrichtungen', 'label': "Senioren - Einrichtungen"},
        {'id': 'sicherheit/karneval', 'label': "Sicherheit - Karneval"},
        {'id': 'sicherheit/kriminalitaetsstatistik', 'label': "Sicherheit - Kriminalitätsstatistik"},
        {'id': 'sicherheit/notinseln', 'label': "Sicherheit - Notinseln"},
        {'id': 'sicherheit/ordnungsamt', 'label': "Sicherheit - Ordnungsamt"},
        {'id': 'sicherheit/silvester', 'label': "Sicherheit - Silvester"},
        {'id': 'sozialeHilfen/asylbewerber', 'label': "Soziale Hilfen - Asylwerber"},
        {'id': 'sozialeHilfen/behindertenwohnheime', 'label': "Soziale Hilfen - Behindertenwohnheime"},
        {'id': 'sozialeHilfen/einrichtungen', 'label': "Soziale Hilfen - Einrichtungen"},
        {'id': 'sozialeHilfen/leistungsbezieher', 'label': "Soziale Hilfen - Leistungsbezieher"},
        {'id': 'sozialeHilfen/strassen', 'label': "Soziale Hilfen - Straßen"},
        {'id': 'sozialeHilfen/wohngeld', 'label': "Soziale Hilfen - Wohngeld"},
        {'id': 'sportUndSpielstaetten/belegung', 'label': "Sport- und Spielstätten - Belegung"},
        {'id': 'sportUndSpielstaetten/einrichtungen', 'label': "Sport- und Spielstätten - Einrichtungen"},
        {'id': 'sportUndSpielstaetten/freibaeder', 'label': "Sport- und Spielstätten - Freibäder"},
        {'id': 'stadtarchiv/bestaende', 'label': "Stadtarchiv - Bestände"},
        {'id': 'stadtmarketing/information', 'label': "Stadtmarketing - Information"},
        {'id': 'stadtmarketing/staedterankings', 'label': "Stadtmarketing - Städterankings"},
        {'id': 'stadtmarketing/standortentwicklung', 'label': "Stadtmarketing - Standortentwicklung"},
        {'id': 'stadtmarketing/zahlenUndFakten', 'label': "Stadtmarketing - Zahlen und Fakten"},
        {'id': 'stadtwerke/ausschreibungenVergaben', 'label': "Stadtwerke - Ausschreibungen Vergaben"},
        {'id': 'stadtwerke/immobilienangebote', 'label': "Stadtwerke - Immobilienangebote"},
        {'id': 'stadtwerke/information', 'label': "Stadtwerke - Information"},
        {'id': 'stadtwerke/kennzahlen', 'label': "Stadtwerke - Kennzahlen"},
        {'id': 'steuernUndAbgaben/hundesteuer', 'label': "Steuern und Abgaben - Hundesteuer"},
        {'id': 'steuernUndAbgaben/nettoeinnahmen', 'label': "Steuern und Abgaben - Nettoeinnahmen"},
        {'id': 'theater/besucherzahlen', 'label': "Theater - Besucherzahlen"},
        {'id': 'tiefbau/geschaeftsberichte', 'label': "Tiefbau - Geschäftsberichte"},
        {'id': 'tourismus/campingplaetze', 'label': "Tourismus - Campingplätze"},
        {'id': 'tourismus/gaestezahlen', 'label': "Tourismus - Gästezahlen"},
        {'id': 'tourismus/privatunterkuenfte', 'label': "Tourismus - Privatunterkünfte"},
        {'id': 'tourismus/sehenswuerdigkeiten', 'label': "Tourismus - Sehenswürdigkeiten"},
        {'id': 'tourismus/stadtfuehrungen', 'label': "Tourismus - Stadtführungen"},
        {'id': 'tourismus/uebernachtungen', 'label': "Tourismus - Übernachtungen"},
        {'id': 'umweltschutz/grundwasser', 'label': "Umweltschutz - Grundwasser"},
        {'id': 'umweltschutz/klimabilanz', 'label': "Umweltschutz - Klimabilanz"},
        {'id': 'umweltschutz/messstellen', 'label': "Umweltschutz - Messstellen"},
        {'id': 'umweltschutz/nachhaltigkeit', 'label': "Umweltschutz - Nachhaltigkeit"},
        {'id': 'umweltschutz/trinkwasser', 'label': "Umweltschutz - Trinkwasser"},
        {'id': 'umweltschutz/umweltzonen', 'label': "Umweltschutz - Umweltzonen"},
        {'id': 'vereineVerbaende/einrichtungen', 'label': "Vereine, Verbände - Einrichtungen"},
        {'id': 'volkshochschulen/information', 'label': "Volkshochschulen - Information"},
        {'id': 'volkshochschulen/programm', 'label': "Volkshochschulen - Programm"},
        {'id': 'volkshochschulen/teilnehmer', 'label': "Volkshochschulen - Teilnehmer"},
        {'id': 'volkshochschulen/veranstaltungen', 'label': "Volkshochschulen - Veranstaltungen"},
        {'id': 'wahlen/kandidatenlisten', 'label': "Wahlen - Kandidatenlisten"},
        {'id': 'wahlen/kommunalwahl', 'label': "Wahlen - Kommunalwahl"},
        {'id': 'wahlen/strassen', 'label': "Wahlen - Straßen"},
        {'id': 'wahlen/wahlbeteiligungBundestagswahlen', 'label': "Wahlen - Wahlbeteiligung Bundestagswahlen"},
        {'id': 'wahlen/wahlbezirke', 'label': "Wahlen - Wahlbezirke"},
        {'id': 'wahlen/wahlbteiligungKommunalwahlen', 'label': "Wahlen - Wahlbeteiligung Kommunalwahlen"},
        {'id': 'wahlen/wahlergebnisBeiratswahlen', 'label': "Wahlen - Wahlergebnis Beiratswahlen"},
        {'id': 'wahlen/wahlergebnisBundestagswahlen', 'label': "Wahlen - Wahlergebnis Bundestagswahlen"},
        {'id': 'wahlen/wahlergebnisEuropawahlen', 'label': "Wahlen - Wahlergebnis Europawahlen"},
        {'id': 'wahlen/wahlergebnisKommunalwahlen', 'label': "Wahlen - Wahlergebnis Kommunalwahlen"},
        {'id': 'wahlen/wahlergebnisLandtagswahlen', 'label': "Wahlen - Wahlergebnis Landtagswahlen"},
        {'id': 'wahlen/wahlkreise', 'label': "Wahlen - Wahlkreise"},
        {'id': 'wahlen/wahllokale', 'label': "Wahlen - Wahllokale"},
        {'id': 'websiten/zugriffe', 'label': "Website - Zugriffe"},
        {'id': 'wetter/hitze', 'label': "Wetter - Hitze"},
        {'id': 'wetter/messstellen', 'label': "Wetter - Messstellen"},
        {'id': 'wirtschaft/bueroflaechen', 'label': "Wirtschaft - Büroflächen"},
        {'id': 'wirtschaft/industrieUndGewerbeflaechen', 'label': "Wirtschaft - Industrie- und Gewerbeflächen"},
        {'id': 'wirtschaft/meldungen', 'label': "Wirtschaft - Meldungen"},
        {'id': 'wirtschaft/wirtschaftsfoerderung', 'label': "Wirtschaft - Wirtschaftsförderung"},
        {'id': 'wirtschaft/wirtschaftsstandorte', 'label': "Wirtschaft - Wirtschaftsstandorte"},
        {'id': 'wohnen/bauprojekte', 'label': "Wohnen - Bauprojekte"},
        {'id': 'wohnen/flaechengroessen', 'label': "Wohnen - Flächengrößen"},
        {'id': 'wohnen/fluechtlingsunterbringung', 'label': "Wohnen - Flüchtlingsunterbringung"},
        {'id': 'wohnen/gefoerderterWohnbau', 'label': "Wohnen - geförderter Wohnbau"},
        {'id': 'wohnen/information', 'label': "Wohnen - Information"},
        {'id': 'wohnen/sozialraeume', 'label': "Wohnen - Sozialräume"},
        {'id': 'wohnen/studentenwohnheime', 'label': "Wohnen - Studentenwohnheime"},
        {'id': 'wohnen/wohnplaetze', 'label': "Wohnen - Wohnplätze"},
        {'id': 'wohnen/wohnquartiere', 'label': "Wohnen - Wohnquartiere"},
        {'id': 'wohnen/wohnungseigentum', 'label': "Wohnen - Wohnungseigentum"},
        {'id': 'zivilUndKatastrophenschutz/kampfmittelfunde', 'label': "Zivil- und Katastrophenschutz - Kampfmittelfunde"},
        {'id': 'zivilUndKatastrophenschutz/sirenen', 'label': "Zivil- und Katastrophenschutz - Sirenen"}
    ]

def render_sample_record(value):
    # TODO: that's obviously super inefficient to compute this every time...
    record_dict = {sample_record['id']: sample_record['label'] for sample_record in sample_record_select_options()}
    if value in record_dict:
      return link_to(record_dict[value], f'https://musterdatenkatalog.de/def/musterdatensatz/{value}')
    return ""

def render_govdata_example_link(value):
    govdata_sparql_link = f"https://www.govdata.de/web/guest/sparql-assistent#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fdatensatz%0A%20%20%20%20dct%3Areferences%20%3Chttps%3A%2F%2Fmusterdatenkatalog.de%2Fdef%2Fmusterdatensatz%2F{value}%3E%20%3B%0A%20%20%20%20dct%3Atitle%20%3Ftitle%20%3B%0A%20%20.%0A%7D%20&endpoint=https%3A%2F%2Fwww.govdata.de%2Fsparql&requestMethod=GET&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=text%2Fturtle%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bxml%2C*%2F*%3Bq%3D0.9&outputFormat=table"
    return link_to("Beispiele bei GovData.de", govdata_sparql_link)

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
    user = model.User.get(str(user_name))
    return user.sysadmin

def first_group_name(data_dict):
    groups = data_dict.get('groups', [])
    if len(groups) > 0:
        return groups[0].get('name', None)
    return None

def show_warning():
    '''Return the setting for the berlintheme.show_warning config setting.'''
    _show_warning = toolkit.asbool(config.get('berlintheme.show_warning', False))
    return _show_warning

def warning_text():
    '''Return the warning text as set in the berlintheme.warning config setting,
    or the default 'Warning'.'''
    return config.get('berlintheme.warning', 'Warning')
