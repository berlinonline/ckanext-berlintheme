# coding: utf-8

import logging
from ckan.lib.helpers import link_to
import ckan.logic as logic
import ckan.model as model
from ckan.common import c, config
from ckanext.berlin_dataset_schema.schema import Schema
import ckan.lib.helpers as helpers
import ckan.plugins.toolkit as toolkit

LOG = logging.getLogger(__name__)
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
      {
        'id': '',
        'label': 'Keine'
      },
      {
        'id': 'abfallentsorgung',
        'label': 'Abfallentsorgung',
        'definition': 'Beseitigung von Müll'
      },
      {
        'id': 'abfallentsorgung/abfallkalender',
        'label': 'Abfallentsorgung – Abfallkalender',
        'definition': 'Auflistung der Müllabfuhrtermine nach Abfallkategorie und Ort'
      },
      {
        'id': 'abfallentsorgung/abfallmenge',
        'label': 'Abfallentsorgung – Abfallmenge',
        'definition': 'Menge des entsorgten Mülls nach unterschiedlichen Abfallarten'
      },
      {
        'id': 'abfallentsorgung/abgabestelle',
        'label': 'Abfallentsorgung – Abgabestelle',
        'definition': 'Ort, an dem bestimmte Müllkategorien abgegeben werden können'
      },
      {
        'id': 'abfallentsorgung/container',
        'label': 'Abfallentsorgung – Container',
        'definition': 'Standorte der Großraumbehälter zur Sammlung, Zwischenlagerung und zum Transport von Müll'
      },
      {
        'id': 'abfallentsorgung/entwaesserung',
        'label': 'Abfallentsorgung – Entwässerung',
        'definition': 'Statistiken zum Abführen von [Ab]wasser durch künstliche und natürliche Einrichtungen'
      },
      {
        'id': 'abfallentsorgung/muellgebuehr',
        'label': 'Abfallentsorgung – Müllgebühr',
        'definition': 'Entgelt für die Abfallentsorgung'
      },
      {
        'id': 'abfallentsorgung/strassenreinigung',
        'label': 'Abfallentsorgung – Straßenreinigung',
        'definition': 'Reinigung öffentlicher Straßen und Plätze'
      },
      {
        'id': 'bau',
        'label': 'Bau',
        'definition': 'Bauen, Errichten, Herstellen'
      },
      {
        'id': 'bau/baufertigstellung',
        'label': 'Bau – Baufertigstellung',
        'definition': 'Bauvorhaben, deren Bauarbeiten weitgehend abgeschlossen sind'
      },
      {
        'id': 'bau/baugenehmigung',
        'label': 'Bau – Baugenehmigung',
        'definition': 'Bauaufsichtsbehördlich erteilte Genehmigung zur Errichtung, Änderung oder Beseitigung eines Baus'
      },
      {
        'id': 'bau/baustelle',
        'label': 'Bau – Baustelle',
        'definition': 'Orte, an denen Bauwerke errichtet, umgebaut oder abgerissen werden'
      },
      {
        'id': 'bau/bauvorhaben',
        'label': 'Bau – Bauvorhaben',
        'definition': 'Gesamter Planungs- und Arbeitsprozess zum Herstellen oder Verändern eines Bauobjekts'
      },
      {
        'id': 'bau/brunnen',
        'label': 'Bau – Brunnen',
        'definition': 'Brunnen und Teichfontänen'
      },
      {
        'id': 'bau/grundstuecksbewertung',
        'label': 'Bau – Grundstücksbewertung',
        'definition': 'Wertermittlung für bebaute und unbebaute Grundstücke und grundstücksgleiche Rechte (Immobilien)'
      },
      {
        'id': 'bau/tiefbau',
        'label': 'Bau – Tiefbau',
        'definition': 'Angaben zum Tätigkeitsbereich der Tiefbauämter'
      },
      {
        'id': 'bau/wohnungsbestand',
        'label': 'Bau – Wohnungsbestand',
        'definition': 'Wohngebäudebestand, Gesamtzahl der in einem Gebiet an einem Stichtag vorhandenen Häuser und Wohnungen'
      },
      {
        'id': 'bevoelkerungsstruktur',
        'label': 'Bevölkerungsstruktur',
        'definition': 'Zusammensetzung einer Bevölkerung nach bestimmten Merkmalen, die deren Charakteristika beschreiben'
      },
      {
        'id': 'bevoelkerungsstruktur/demografiebericht',
        'label': 'Bevölkerungsstruktur – Demografiebericht',
        'definition': 'Bericht, der die demografische Entwicklung für Kommunen darstellt'
      },
      {
        'id': 'bevoelkerungsstruktur/einwohnerzahl',
        'label': 'Bevölkerungsstruktur – Einwohnerzahl',
        'definition': 'Gesamtzahl der Einwohnerinnen und Einwohner'
      },
      {
        'id': 'bevoelkerungsstruktur/haushaltszusammensetzung',
        'label': 'Bevölkerungsstruktur – Haushaltszusammensetzung',
        'definition': 'Personen, die in einer gemeinsamen Wohnung leben'
      },
      {
        'id': 'bevoelkerungsstruktur/migrationshintergrund',
        'label': 'Bevölkerungsstruktur – Migrationshintergrund',
        'definition': 'Daten zur Bevölkerungszusammensetzung im Hinblick auf den Faktor \'Migrationshintergrund\''
      },
      {
        'id': 'bevoelkerungsstruktur/religionszugehoerigkeit',
        'label': 'Bevölkerungsstruktur – Religionszugehörigkeit',
        'definition': 'Zugehörigkeit einer Person zu einer bestimmten Religionsgemeinschaft'
      },
      {
        'id': 'bevoelkerungsstruktur/staatsangehoerigkeit',
        'label': 'Bevölkerungsstruktur – Staatsangehörigkeit',
        'definition': 'Angaben zur Staatsangehörigkeit der Bevölkerung'
      },
      {
        'id': 'bevoelkerungsstruktur/vorname',
        'label': 'Bevölkerungsstruktur – Vorname',
        'definition': 'Statistiken zu vergebenen Vornamen'
      },
      {
        'id': 'bildung',
        'label': 'Bildung',
        'definition': 'Vermittlung von Fertigkeiten und Wissen durch eine dazu befugte Einrichtung, beispielsweise eine staatliche Schule, eine Hochschule oder ein privates Unternehmen'
      },
      {
        'id': 'bildung/ausbildung',
        'label': 'Bildung – Ausbildung',
        'definition': 'Ausbildungseinrichtungen'
      },
      {
        'id': 'bildung/bibliothek/ausleihe',
        'label': 'Bildung – Bibliothek - Ausleihe',
        'definition': 'Verliehene Bibliotheksmedien'
      },
      {
        'id': 'bildung/bibliothek/bestand',
        'label': 'Bildung – Bibliothek - Bestand',
        'definition': 'Gesamtheit der in Bibliotheken gesammelten Publikationen'
      },
      {
        'id': 'bildung/bibliothek/besucherzahl',
        'label': 'Bildung – Bibliothek - Besucherzahl',
        'definition': 'Anzahl der Besucherinnen und Besucher von Bibliotheken'
      },
      {
        'id': 'bildung/bibliothek/budget',
        'label': 'Bildung – Bibliothek - Budget',
        'definition': 'Finanzpläne von Bibliotheken'
      },
      {
        'id': 'bildung/bibliothek/standort',
        'label': 'Bildung – Bibliothek - Standort',
        'definition': 'Standorte von Bibliotheken'
      },
      {
        'id': 'bildung/hochschule/standort',
        'label': 'Bildung – Hochschule - Standort',
        'definition': 'Standorte von Hochschulen'
      },
      {
        'id': 'bildung/hochschule/studentenwohnheim',
        'label': 'Bildung – Hochschule - Studentenwohnheim',
        'definition': 'Unterkünfte für Studierende'
      },
      {
        'id': 'bildung/hochschule/studierendenzahl',
        'label': 'Bildung – Hochschule - Studierendenzahl',
        'definition': 'Anzahl der Studierenden an einer Hochschule'
      },
      {
        'id': 'bildung/kindertageseinrichtung/betreuungsplatz',
        'label': 'Bildung – Kindertageseinrichtung - Betreuungsplatz',
        'definition': 'Zur Verfügung stehende Betreuungsplätze in Kindertagesstätten'
      },
      {
        'id': 'bildung/kindertageseinrichtung/standort',
        'label': 'Bildung – Kindertageseinrichtung - Standort',
        'definition': 'Standorte von Einrichtungen, in denen Kinder ganztägig betreut werden'
      },
      {
        'id': 'bildung/musikschule/teilnehmerzahl',
        'label': 'Bildung – Musikschule - Teilnehmerzahl',
        'definition': 'Zahl der Personen, die an Unterricht oder Veranstaltungen der Musikschulen teilnehmen'
      },
      {
        'id': 'bildung/musikschule/unterrichtsangebot',
        'label': 'Bildung – Musikschule - Unterrichtsangebot',
        'definition': 'Fächer, die an Musikschulen unterricht werden'
      },
      {
        'id': 'bildung/schule/internetanbindung',
        'label': 'Bildung – Schule - Internetanbindung',
        'definition': 'Anbindung von Schulen ins Internet'
      },
      {
        'id': 'bildung/schule/schuelerzahl',
        'label': 'Bildung – Schule - Schülerzahl',
        'definition': 'Anzahl der Schülerinnen und Schüler'
      },
      {
        'id': 'bildung/schule/schulangebot',
        'label': 'Bildung – Schule - Schulangebot',
        'definition': 'Verzeichnisse der zur Verfügung stehenden Schulen bzw. deren Angebote'
      },
      {
        'id': 'bildung/schule/schuleingangsuntersuchung',
        'label': 'Bildung – Schule - Schuleingangsuntersuchung',
        'definition': 'Gesetzlich vorgeschriebene Schulneulingsuntersuchung auf Einladung des Gesundheitsamtes vor der Aufnahme in die erste Jahrgangsstufe der Grundschule'
      },
      {
        'id': 'bildung/schule/schulentwicklungsplan',
        'label': 'Bildung – Schule - Schulentwicklungsplan',
        'definition': 'Planungs- und Steuerungsinstrument für die Umsetzung schulischer Entwicklungsvorhaben'
      },
      {
        'id': 'bildung/schule/standort',
        'label': 'Bildung – Schule - Standort',
        'definition': 'Standorte, an denen sich Schulen befinden'
      },
      {
        'id': 'bildung/schule/wunschschule',
        'label': 'Bildung – Schule - Wunschschule',
        'definition': 'Angaben zur Wahl der Erstwunsch-Schule'
      },
      {
        'id': 'bildung/volkshochschule/teilnehmerzahl',
        'label': 'Bildung – Volkshochschule - Teilnehmerzahl',
        'definition': 'Anzahl der am Angebot der Erwachsenenbildungsinstitute teilnehmenden Personen'
      },
      {
        'id': 'bildung/volkshochschule/veranstaltung',
        'label': 'Bildung – Volkshochschule - Veranstaltung',
        'definition': 'Events, die an Erwachsenenbildungsinstituten stattfinden'
      },
      {
        'id': 'buergerservice',
        'label': 'Bürgerservice',
        'definition': 'Zentrale Anlaufstelle, die Bürgerinnen und Bürgern Informationen und die Erledigung ihrer Anliegen aus erster Hand anbietet'
      },
      {
        'id': 'buergerservice/anliegenmanagement',
        'label': 'Bürgerservice – Anliegenmanagement',
        'definition': 'Systeme, mit denen Anliegen, Beschwerden, Hinweise und Wünsche von Nutzerinnen und Nutzern öffentlicher Dienste eingereicht werden'
      },
      {
        'id': 'buergerservice/dienstleistung',
        'label': 'Bürgerservice – Dienstleistung',
        'definition': 'Serviceangebote der Bürgerservicestellen'
      },
      {
        'id': 'buergerservice/hundekottuete',
        'label': 'Bürgerservice – Hundekottüte',
        'definition': 'Standorte von Hundekotbeutelstationen'
      },
      {
        'id': 'buergerservice/telefonverzeichnis',
        'label': 'Bürgerservice – Telefonverzeichnis',
        'definition': 'Telefonnummern von Mitarbeiterinnen und Mitarbeitern der Verwaltung'
      },
      {
        'id': 'buergerservice/termin',
        'label': 'Bürgerservice – Termin',
        'definition': 'Termine und Öffnungszeiten von Einrichtungen der Kommunalverwaltung'
      },
      {
        'id': 'buergerservice/wartezeit',
        'label': 'Bürgerservice – Wartezeit',
        'definition': 'Wartezeiten in Einrichtungen der Kommunalverwaltung'
      },
      {
        'id': 'digitalisierung',
        'label': 'Digitalisierung',
        'definition': 'Digitale Transformation und Durchdringung aller Bereiche von Wirtschaft, Staat, Gesellschaft und Alltag'
      },
      {
        'id': 'digitalisierung/openData/planung',
        'label': 'Digitalisierung – Open Data - Planung',
        'definition': 'Angaben zur Durchführung von Initiativen für offene Verwaltungsdaten'
      },
      {
        'id': 'digitalisierung/openData/zugriffszahl',
        'label': 'Digitalisierung – Open Data - Zugriffszahl',
        'definition': 'Zahl der Aufrufe von offenen Verwaltungsdaten'
      },
      {
        'id': 'digitalisierung/website',
        'label': 'Digitalisierung – Website',
        'definition': 'Zugriffstatistiken der kommunalen Websites'
      },
      {
        'id': 'digitalisierung/wlanUndMobilfunk',
        'label': 'Digitalisierung – WLAN und Mobilfunk',
        'definition': 'Standorte von WLAN-Hotspots, Freifunkrouter und Mobilfunkstandorte'
      },
      {
        'id': 'energie',
        'label': 'Energie',
        'definition': 'Fähigkeit, mechanische Arbeit zu verrichten, Wärme abzugeben oder Licht auszustrahlen'
      },
      {
        'id': 'energie/energiebericht',
        'label': 'Energie – Energiebericht',
        'definition': 'Darstellungen im Bereich Energiemanagement und der Erfolge von durchgeführten Maßnahmen'
      },
      {
        'id': 'energie/solar',
        'label': 'Energie – Solar',
        'definition': 'Solarenergiekataster bzw. Angaben zur erzeugten Solarenergie'
      },
      {
        'id': 'energie/stromversorgung',
        'label': 'Energie – Stromversorgung',
        'definition': 'Kennzahlen zur Stromversorgung in einer Kommune'
      },
      {
        'id': 'energie/waermeversorgung',
        'label': 'Energie – Wärmeversorgung',
        'definition': 'Kennzahlen zur Wärmeversorgung in einer Kommune'
      },
      {
        'id': 'energie/wasserversorgung',
        'label': 'Energie – Wasserversorgung',
        'definition': 'Kennzahlen zur Wasserversorgung in einer Kommune'
      },
      {
        'id': 'energie/windenergie',
        'label': 'Energie – Windenergie',
        'definition': 'Kennzahlen zur Versorgung mit Windenergie in einer Kommune'
      },
      {
        'id': 'finanzen',
        'label': 'Finanzen',
        'definition': 'Finanzielle Gebahrung einer Kommune'
      },
      {
        'id': 'finanzen/haushalt/ausserplanmaessigeAufwendungen',
        'label': 'Finanzen – Haushalt - Außerplanmäßige Aufwendung',
        'definition': 'Aufwendungen oder Auszahlungen, für die im Haushaltsplan keine Ermächtigungen veranschlagt und keine aus den Vorjahren übertragenen Ermächtigungen verfügbar sind'
      },
      {
        'id': 'finanzen/haushalt/controlling',
        'label': 'Finanzen – Haushalt - Controlling',
        'definition': 'Überwachung des kommunalen Haushalts'
      },
      {
        'id': 'finanzen/haushalt/jahresabschluss',
        'label': 'Finanzen – Haushalt - Jahresabschluss',
        'definition': 'Haushaltsrechnungen von Kommunen'
      },
      {
        'id': 'finanzen/haushalt/plan',
        'label': 'Finanzen – Haushalt - Plan',
        'definition': 'Kommunale Haushaltspläne'
      },
      {
        'id': 'finanzen/haushalt/produktplan',
        'label': 'Finanzen – Haushalt - Produktplan',
        'definition': 'Von einer öffentlichen Verwaltung erstellter, verwaltungsspezifischer Gliederungsplan, der die Produktstruktur im Haushaltsplan festlegt'
      },
      {
        'id': 'finanzen/haushalt/satzung',
        'label': 'Finanzen – Haushalt - Satzung',
        'definition': 'Rechtsgrundlage für den Vollzug des Haushaltsplans in der kommunalen Verwaltung, der von der Gemeindevertretung oder dem Kreistag in öffentlicher Sitzung beschlossen wird'
      },
      {
        'id': 'finanzen/haushalt/sponsoring',
        'label': 'Finanzen – Haushalt - Sponsoring',
        'definition': 'Unterstützungen seitens der Kommunen durch finanzielle Mittel bzw. Sach- oder Dienstleistungen'
      },
      {
        'id': 'finanzen/haushalt/zuwendungUndFoerderung',
        'label': 'Finanzen – Haushalt - Zuwendung und Förderung',
        'definition': 'Finanzielle Zuwendungen aus dem kommunalen Budget'
      },
      {
        'id': 'finanzen/steuernUndAbgaben',
        'label': 'Finanzen – Steuern und Abgaben',
        'definition': 'Aufkommen an Steuern, Beiträgen und Gebühren'
      },
      {
        'id': 'floraUndFauna',
        'label': 'Flora und Fauna',
        'definition': 'Pflanzen- und Tierwelt'
      },
      {
        'id': 'floraUndFauna/baumbestand/baumfaellung',
        'label': 'Flora und Fauna – Baumbestand - Baumfällung',
        'definition': 'Umschneiden von Bäumen'
      },
      {
        'id': 'floraUndFauna/baumbestand/baumkataster',
        'label': 'Flora und Fauna – Baumbestand - Baumkataster',
        'definition': 'Verzeichnis, in dem Bäume inklusive Standort und weiteren Informationen verwaltet werden'
      },
      {
        'id': 'floraUndFauna/flaeche/ausgleichsflaeche',
        'label': 'Flora und Fauna – Fläche - Ausgleichsfläche',
        'definition': 'Flächen für den Naturschutz, die bei Eingriffen in Natur und Landschaft, wie z. B. größere Bauprojekte, dafür sorgen, dass ein gewisser Ausgleich für negative ökologische Folgen geschaffen wird'
      },
      {
        'id': 'floraUndFauna/flaeche/biotopflaeche',
        'label': 'Flora und Fauna – Fläche - Biotopfläche',
        'definition': 'Verzeichnis der Biotope in den Kommunen'
      },
      {
        'id': 'floraUndFauna/flaeche/gruenflaecheUndGruenflaechenkataster',
        'label': 'Flora und Fauna – Fläche - Grünfläche und Grünflächenkataster',
        'definition': 'Verzeichnis der kommunalen Grünflächen meist mit Koppelung an ein Geoinformationssystem mit Angaben wie Fläche, Standort, Pflanzenbestand und Pflegemaßnahmen'
      },
      {
        'id': 'floraUndFauna/flaeche/hundewiese',
        'label': 'Flora und Fauna – Fläche - Hundewiese',
        'definition': 'Standorte der kommunalen Hundeauslaufgebiete'
      },
      {
        'id': 'floraUndFauna/flaeche/jagdbezirk',
        'label': 'Flora und Fauna – Fläche - Jagdbezirk',
        'definition': 'Kommunale Gebiete, in denen die Jagd ausgeübt wird'
      },
      {
        'id': 'floraUndFauna/flaeche/naturschutzgebiet',
        'label': 'Flora und Fauna – Fläche - Naturschutzgebiet',
        'definition': 'Kommunale Gebiete, die unter Naturschutz stehen'
      },
      {
        'id': 'floraUndFauna/flaeche/waldflaeche',
        'label': 'Flora und Fauna – Fläche - Waldfläche',
        'definition': 'Bewaldete kommunale Gebiete'
      },
      {
        'id': 'floraUndFauna/gewaesser/pegelstand',
        'label': 'Flora und Fauna – Gewässer - Pegelstand',
        'definition': 'Wasserstände kommunaler Gewässer'
      },
      {
        'id': 'floraUndFauna/gewaesser/wasserflaeche',
        'label': 'Flora und Fauna – Gewässer - Wasserfläche',
        'definition': 'Kommunale Gewässer'
      },
      {
        'id': 'floraUndFauna/urbanGardening',
        'label': 'Flora und Fauna – Urban Gardening',
        'definition': 'Kleinräumige, gärtnerisch genutzte städtische Flächen'
      },
      {
        'id': 'freizeit',
        'label': 'Freizeit',
        'definition': 'kommunale Freizeitangebote'
      },
      {
        'id': 'freizeit/badUndFreibad',
        'label': 'Freizeit – Bad und Freibad',
        'definition': 'Standorte und Kennzahlen der kommunalen Schwimmbäder'
      },
      {
        'id': 'freizeit/ferienangebot',
        'label': 'Freizeit – Ferienangebot',
        'definition': 'Während der Schulferien angebotene Freizeitaktivitäten für Kinder und Jugendliche '
      },
      {
        'id': 'freizeit/grillplatz',
        'label': 'Freizeit – Grillplatz',
        'definition': 'Standorte öffentlicher Grillstellen'
      },
      {
        'id': 'freizeit/jugendeinrichtung',
        'label': 'Freizeit – Jugendeinrichtung',
        'definition': 'Standorte bzw. Angebote der Einrichtungen der kommunalen Jugendhilfe'
      },
      {
        'id': 'freizeit/sitzgelegenheit',
        'label': 'Freizeit – Sitzgelegenheit',
        'definition': 'Sitzplätze im öffentlichen Raum'
      },
      {
        'id': 'freizeit/spielplatzUndSpielstaette',
        'label': 'Freizeit – Spielplatz und Spielstätte',
        'definition': 'Standorte bzw. Kennzahlen der kommunalen Spielanlagen'
      },
      {
        'id': 'freizeit/verein',
        'label': 'Freizeit – Verein',
        'definition': 'Informationen zu Vereinen in Kommunen'
      },
      {
        'id': 'geschichte',
        'label': 'Geschichte',
        'definition': 'Daten zum politischen, kulturellen und gesellschaftlichen Werdegang, Entwicklungsprozess einer Kommune'
      },
      {
        'id': 'geschichte/quelle/archivbestand',
        'label': 'Geschichte – Quelle - Archivbestand',
        'definition': 'Bestände kommunaler Archive'
      },
      {
        'id': 'geschichte/quelle/entschaedigung',
        'label': 'Geschichte – Quelle - Entschädigung',
        'definition': 'Kommunale Entschädigungsakten'
      },
      {
        'id': 'geschichte/quelle/historischeKarte',
        'label': 'Geschichte – Quelle - Historische Karte',
        'definition': 'Daten zu historischen Landkarten'
      },
      {
        'id': 'geschichte/quelle/historischeLuftaufnahme',
        'label': 'Geschichte – Quelle - Historische Luftaufnahme',
        'definition': 'Daten zu historischen Fotoaufnahmen der Kommunen aus der Luft'
      },
      {
        'id': 'geschichte/quelle/personalverzeichnis',
        'label': 'Geschichte – Quelle - Personalverzeichnis',
        'definition': 'Kontaktliste kommunaler Mitarbeiterinnen und Mitarbeiter'
      },
      {
        'id': 'geschichte/standortMitGeschichte',
        'label': 'Geschichte – Standort mit Geschichte',
        'definition': 'Orte mit geschichtlicher Relevanz'
      },
      {
        'id': 'gesundheit',
        'label': 'Gesundheit',
        'definition': 'Daten zu kommunalen Gesundheitsdienstleistungen und -einrichtungen'
      },
      {
        'id': 'gesundheit/apotheke',
        'label': 'Gesundheit – Apotheke',
        'definition': 'Standorte und weitere Angaben zu Apotheken'
      },
      {
        'id': 'gesundheit/arzt',
        'label': 'Gesundheit – Arzt',
        'definition': 'Daten zu den Ärztinnen und Ärzten'
      },
      {
        'id': 'gesundheit/gesundheitsberichterstattung',
        'label': 'Gesundheit – Gesundheitsberichterstattung',
        'definition': 'Kommunale Gesundheitsberichte'
      },
      {
        'id': 'gesundheit/hebamme',
        'label': 'Gesundheit – Hebamme',
        'definition': 'Listen aller im Kommunalgebiet tätigen Hebammen'
      },
      {
        'id': 'gesundheit/infektion',
        'label': 'Gesundheit – Infektion',
        'definition': 'Infektionsgeschehen in den Kommunen'
      },
      {
        'id': 'gesundheit/krankenhaus',
        'label': 'Gesundheit – Krankenhaus',
        'definition': 'Standorte und Kennzahlen zu Krankenhäusern in einer Kommune'
      },
      {
        'id': 'gesundheit/oeffentlicheToilette',
        'label': 'Gesundheit – Öffentliche Toilette',
        'definition': 'Informationen zu Standort und Austattung der öffentlichen Bedürfnisanstalten in einer Kommune'
      },
      {
        'id': 'gesundheit/rettungsdienst/defibrillator',
        'label': 'Gesundheit – Rettungsdienst - Defibrillator',
        'definition': 'Standorte kommunaler Defibrillatoren'
      },
      {
        'id': 'gesundheit/rettungsdienst/rettungsdiensteinsatz',
        'label': 'Gesundheit – Rettungsdienst - Rettungsdiensteinsatz',
        'definition': 'Kennzahlen zu Einsätzen durch die kommunalen Rettungsdienste'
      },
      {
        'id': 'justiz',
        'label': 'Justiz',
        'definition': 'Für die Ausübung der Justiz verantwortliche Behörden und Einrichtungen'
      },
      {
        'id': 'justiz/gesetzestext',
        'label': 'Justiz – Gesetzestext',
        'definition': 'Wortlaut eines Gesetzes'
      },
      {
        'id': 'justiz/justizeinrichtung',
        'label': 'Justiz – Justizeinrichtung',
        'definition': 'Angaben über kommunale Justizstandorte'
      },
      {
        'id': 'klimaschutzUndUmweltschutz',
        'label': 'Klimaschutz und Umweltschutz',
        'definition': 'Daten zu Witterung und Wettererscheinungen bzw.  zum Schutz der natürlichen Umwelt'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/berichtUndAnalyse/klimabilanz',
        'label': 'Klimaschutz und Umweltschutz – Bericht und Analyse - Klimabilanz',
        'definition': 'Kennzahlen zur Klimabilanz der Kommunen'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/berichtUndAnalyse/luftUndEmission',
        'label': 'Klimaschutz und Umweltschutz – Bericht und Analyse - Luft und Emission',
        'definition': 'Kennzahlen zu Luft- und Emissionswerten'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/berichtUndAnalyse/verkehrsmessung',
        'label': 'Klimaschutz und Umweltschutz – Bericht und Analyse - Verkehrsmessung',
        'definition': 'Kennzahlen zum Verkehrsaufkommen in einer Kommune'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/berichtUndAnalyse/wasser',
        'label': 'Klimaschutz und Umweltschutz – Bericht und Analyse - Wasser',
        'definition': 'Kennzahlen zu Wasser in einer Kommune'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/radioaktivitaetsmessung',
        'label': 'Klimaschutz und Umweltschutz – Radioaktivitätsmessung',
        'definition': 'Kennzahlen zu Radioaktivität in einer Kommune'
      },
      {
        'id': 'klimaschutzUndUmweltschutz/umweltzone',
        'label': 'Klimaschutz und Umweltschutz – Umweltzone',
        'definition': 'Daten zu den in einer Kommune eingerichteten Gebieten, in denen nur Kfz mit Feinstaubplakette fahren dürfen'
      },
      {
        'id': 'kultur',
        'label': 'Kultur',
        'definition': 'Daten zu Standort bzw. Angebot an geistigen, künstlerischen, gestaltenden Leistungen einer Kommune wie etwa Kunstwerke, Bauwerke (Museen, Theater, Denkmäler, Kirchen, Friedhöfe) usw.'
      },
      {
        'id': 'kultur/denkmal',
        'label': 'Kultur – Denkmal',
        'definition': 'Standorte und weitere Angaben zu Denkmälerm bzw. Erinnerungsorten in Kommunen'
      },
      {
        'id': 'kultur/friedhof/grabstaette',
        'label': 'Kultur – Friedhof - Grabstätte',
        'definition': 'Standorte und Eigenschaften von Stellen, an denen Tote beerdigt sind'
      },
      {
        'id': 'kultur/friedhof/standort',
        'label': 'Kultur – Friedhof - Standort',
        'definition': 'Standorte der Friedhöfe'
      },
      {
        'id': 'kultur/kunstwerk',
        'label': 'Kultur – Kunstwerk',
        'definition': 'Daten zu Erzeugnissen künstlerischen Schaffens im öffentlichen Raum der Kommunen'
      },
      {
        'id': 'kultur/lehrpfadUndWanderpfad',
        'label': 'Kultur – Lehrpfad und Wanderpfad',
        'definition': 'Daten zu Freizeitwegen inkl. gestalteten [Themen]wegen mit dem Ziel der Wissensvermittlung'
      },
      {
        'id': 'kultur/museum/besucherzahl',
        'label': 'Kultur – Museum - Besucherzahl',
        'definition': 'Frequentierungszahlen in Museen'
      },
      {
        'id': 'kultur/museum/standort',
        'label': 'Kultur – Museum - Standort',
        'definition': 'Standorte der Museen in Kommunen'
      },
      {
        'id': 'kultur/religioeseEinrichtung',
        'label': 'Kultur – religiöse Einrichtung',
        'definition': 'Standorte bzw. Kennzahlen zu Sakralbauten, Gotteshäusern, Glaubenseinrichtungen'
      },
      {
        'id': 'kultur/theater/besucherzahl',
        'label': 'Kultur – Theater - Besucherzahl',
        'definition': 'Anzahl der Besucherinnen und Besucher von Theatern'
      },
      {
        'id': 'kultur/theater/programm',
        'label': 'Kultur – Theater - Programm',
        'definition': 'Informationen zu Theatervorstellungen'
      },
      {
        'id': 'kultur/veranstaltung/angebot',
        'label': 'Kultur – Veranstaltung - Angebot',
        'definition': 'Informationen zu angebotenen Veranstaltungen'
      },
      {
        'id': 'kultur/veranstaltung/besucherzahl',
        'label': 'Kultur – Veranstaltung - Besucherzahl',
        'definition': 'Anzahl der Besucherinnen und Besucher einer Veranstaltung'
      },
      {
        'id': 'oeffentlichkeitsarbeit',
        'label': 'Öffentlichkeitsarbeit',
        'definition': 'öffentliche Kommunikation'
      },
      {
        'id': 'oeffentlichkeitsarbeit/pressemitteilungUndVeroeffentlichung',
        'label': 'Öffentlichkeitsarbeit – Pressemitteilung und Veröffentlichung',
        'definition': 'Medienaussendungen und Pressemeldungen'
      },
      {
        'id': 'oeffentlichkeitsarbeit/stadtmarketing',
        'label': 'Öffentlichkeitsarbeit – Stadtmarketing',
        'definition': 'Gesamtheit der Maßnahmen zur Imageförderung einer Stadt'
      },
      {
        'id': 'politischePartizipation',
        'label': 'Politische Partizipation',
        'definition': 'Teilhabe und Beteiligung von Bürgerinnen und Bürgern an politischen Willensbildungs- und Entscheidungsprozessen'
      },
      {
        'id': 'politischePartizipation/buergerbeteiligung/buergerentscheid',
        'label': 'Politische Partizipation – Bürgerbeteiligung - Bürgerentscheid',
        'definition': 'Entscheidung einer wichtigen Angelegenheit der Kommune durch die Bürgerinnen und Bürger'
      },
      {
        'id': 'politischePartizipation/buergerbeteiligung/buergerhaushalt',
        'label': 'Politische Partizipation – Bürgerbeteiligung - Bürgerhaushalt',
        'definition': 'Direkte kommunale Bürgerbeteiligung, bei der die Bürgerinnen und Bürger über Teile der Haushaltsmittel mitbestimmen'
      },
      {
        'id': 'politischePartizipation/buergerbeteiligung/entwicklungUndInformation',
        'label': 'Politische Partizipation – Bürgerbeteiligung - Entwicklung und Information',
        'definition': 'Information über und Weiterentwicklung der Bürgerbeteiligung'
      },
      {
        'id': 'politischePartizipation/buergerbeteiligung/umfrage',
        'label': 'Politische Partizipation – Bürgerbeteiligung - Umfrage',
        'definition': 'Daten zu Befragungen von Bürgerinnen und Bürgern zu bestimmten Themen der Verwaltung'
      },
      {
        'id': 'politischePartizipation/politischeVertretung/buergermeister',
        'label': 'Politische Partizipation – Politische Vertretung - Bürgermeister',
        'definition': 'Angaben zu den Bürgermeisterinnen und Bürgermeistern der Kommunen'
      },
      {
        'id': 'politischePartizipation/politischeVertretung/gremium',
        'label': 'Politische Partizipation – Politische Vertretung - Gremium',
        'definition': 'Informationen zu den beschlussfassenden Ausschüssen der Kommunen'
      },
      {
        'id': 'politischePartizipation/politischeVertretung/mandatstraeger',
        'label': 'Politische Partizipation – Politische Vertretung - Mandatsträger',
        'definition': 'Informationen zu Mandatsträgerinnen und Mandatsträgern der Kommunen'
      },
      {
        'id': 'politischePartizipation/verband',
        'label': 'Politische Partizipation – Verband',
        'definition': 'Zusammenschluss mehrerer kleinerer Vereinigungen oder Einzelpersonen zur Durchsetzung gemeinsamer Interessen'
      },
      {
        'id': 'politischePartizipation/wahl/beiratswahl',
        'label': 'Politische Partizipation – Wahl - Beiratswahl',
        'definition': 'Informationen über die Wahlen kommunaler Beiräte'
      },
      {
        'id': 'politischePartizipation/wahl/bundestagswahl',
        'label': 'Politische Partizipation – Wahl - Bundestagswahl',
        'definition': 'Wahleinrichtungen bzw. Wahlergebnisse der Bundestagswahl'
      },
      {
        'id': 'politischePartizipation/wahl/europawahl',
        'label': 'Politische Partizipation – Wahl - Europawahl',
        'definition': 'Wahleinrichtungen bzw. Wahlergebnisse der Europawahl'
      },
      {
        'id': 'politischePartizipation/wahl/kandidatenliste',
        'label': 'Politische Partizipation – Wahl - Kandidatenliste',
        'definition': 'Wahlvorschläge der Kommunen'
      },
      {
        'id': 'politischePartizipation/wahl/kommunalwahl',
        'label': 'Politische Partizipation – Wahl - Kommunalwahl',
        'definition': 'Wahleinrichtungen bzw. Wahlergebnisse von Kommunalwahlen'
      },
      {
        'id': 'politischePartizipation/wahl/landtagswahl',
        'label': 'Politische Partizipation – Wahl - Landtagswahl',
        'definition': 'Wahleinrichtungen bzw. Wahlergebnisse der Landtagswahl'
      },
      {
        'id': 'politischePartizipation/wahl/strassenverzeichnis',
        'label': 'Politische Partizipation – Wahl - Straßenverzeichnis',
        'definition': 'Für Wahlen erstelltes Verzeichnis der Straßen und Plätze einer Kommune nach Stimmbezirk, Wahlbezirk, Wahlkreis'
      },
      {
        'id': 'politischePartizipation/wahl/verbundwahl',
        'label': 'Politische Partizipation – Wahl - Verbundwahl',
        'definition': 'Durch Zusammenlegung gleichzeitig stattfindende Wahlen'
      },
      {
        'id': 'politischePartizipation/wahl/wahlkreisUndWahlbezirk',
        'label': 'Politische Partizipation – Wahl - Wahlkreis und Wahlbezirk',
        'definition': 'Daten zu Wahlkreisen und Wahlbezirken'
      },
      {
        'id': 'politischePartizipation/wahl/wahllokal',
        'label': 'Politische Partizipation – Wahl - Wahllokal',
        'definition': 'Daten zu Orten der Wahlaustragung'
      },
      {
        'id': 'raumplanung',
        'label': 'Raumplanung',
        'definition': 'Daten zu Raumordnung, Raumplanung und Raumentwicklung'
      },
      {
        'id': 'raumplanung/bauleitplan',
        'label': 'Raumplanung – Bauleitplan',
        'definition': 'Daten zu städtebaulichen Entwicklungsplänen'
      },
      {
        'id': 'raumplanung/bebauungsplan',
        'label': 'Raumplanung – Bebauungsplan',
        'definition': 'Kommunale Plänen, nach denen Flächen bebaut werden sollen'
      },
      {
        'id': 'raumplanung/flaechennutzung',
        'label': 'Raumplanung – Flächennutzung',
        'definition': 'Nutzung größerer Flächen einer Kommune für bestimmte Zwecke'
      },
      {
        'id': 'raumplanung/liegenschaft/grundstueckUndGebaeude',
        'label': 'Raumplanung – Liegenschaft - Grundstück und Gebäude',
        'definition': 'Daten zu kommunalen Liegenschaften'
      },
      {
        'id': 'raumplanung/liegenschaft/liegenschaftskataster',
        'label': 'Raumplanung – Liegenschaft - Liegenschaftskataster',
        'definition': 'Daten zum Grundstücksverzeichnis'
      },
      {
        'id': 'raumplanung/liegenschaft/satzung',
        'label': 'Raumplanung – Liegenschaft - Satzung',
        'definition': 'Satzungen im Bereich Liegenschaften'
      },
      {
        'id': 'raumplanung/orthofoto',
        'label': 'Raumplanung – Orthofoto',
        'definition': 'Verzerrungsfreie, maßstabsgetreue aus Luft- oder Satellitenbildern abgeleitete Abbildungen der Erdoberfläche'
      },
      {
        'id': 'raumplanung/raumgliederung/adresse',
        'label': 'Raumplanung – Raumgliederung - Adresse',
        'definition': 'Daten zu Anschriften'
      },
      {
        'id': 'raumplanung/raumgliederung/block',
        'label': 'Raumplanung – Raumgliederung - Block',
        'definition': 'Beschreibung von Gebieten innerhalb eines Stadtteils, die als Blöcke bezeichnet werden'
      },
      {
        'id': 'raumplanung/raumgliederung/hausnummer',
        'label': 'Raumplanung – Raumgliederung - Hausnummer',
        'definition': 'Daten zu den Nummern der einzelnen Häuser'
      },
      {
        'id': 'raumplanung/raumgliederung/ortsteil',
        'label': 'Raumplanung – Raumgliederung - Ortsteil',
        'definition': 'Daten zur kommunalen Gliederung in Stadtteile'
      },
      {
        'id': 'raumplanung/raumgliederung/postleitzahlengebiet',
        'label': 'Raumplanung – Raumgliederung - Postleitzahlengebiet',
        'definition': 'Postleitzahlen von Städten und Gemeinden'
      },
      {
        'id': 'raumplanung/raumgliederung/stadtgebiet',
        'label': 'Raumplanung – Raumgliederung - Stadtgebiet',
        'definition': 'Informationen zu Stadtgebieten'
      },
      {
        'id': 'raumplanung/raumgliederung/strasse',
        'label': 'Raumplanung – Raumgliederung - Straße',
        'definition': 'Informationen zu Straßen'
      },
      {
        'id': 'raumplanung/sozialraum',
        'label': 'Raumplanung – Sozialraum',
        'definition': 'Daten zu Sozialraum als Stadtplanungs- und Verwaltungskategorie'
      },
      {
        'id': 'raumplanung/stadtplan',
        'label': 'Raumplanung – Stadtplan',
        'definition': 'Kartographische Daten einer Stadt'
      },
      {
        'id': 'sicherheit',
        'label': 'Sicherheit',
        'definition': 'Daten zu kommunalen Sicherheitsthemen'
      },
      {
        'id': 'sicherheit/beleuchtung',
        'label': 'Sicherheit – Beleuchtung',
        'definition': 'Daten zur öffentlichen Beleuchtung'
      },
      {
        'id': 'sicherheit/feuerwehr/feuerwehreinsatz',
        'label': 'Sicherheit – Feuerwehr - Feuerwehreinsatz',
        'definition': 'Daten zu Einsätzen der Feuerwehr in den Kommunen'
      },
      {
        'id': 'sicherheit/feuerwehr/personal',
        'label': 'Sicherheit – Feuerwehr - Personal',
        'definition': 'Daten zu den im Feuerwehrdienst tätigen Einsatzkräften'
      },
      {
        'id': 'sicherheit/feuerwehr/standort',
        'label': 'Sicherheit – Feuerwehr - Standort',
        'definition': 'Verzeichnis der Feuerwehrstandorte'
      },
      {
        'id': 'sicherheit/kriminalitaetsstatistik',
        'label': 'Sicherheit – Kriminalitätsstatistik',
        'definition': 'Daten zur Kriminalität'
      },
      {
        'id': 'sicherheit/ordnungsamt',
        'label': 'Sicherheit – Ordnungsamt',
        'definition': 'Informationen über die Tätigkeit der für die Abwehr von Gefahren für die öffentliche Sicherheit oder Ordnung verantwortliche Organisationseinheit der Kommunalverwaltung'
      },
      {
        'id': 'sicherheit/polizei',
        'label': 'Sicherheit – Polizei',
        'definition': 'Standorte der Polizei'
      },
      {
        'id': 'sicherheit/rettungshilfe/anlaufstelle',
        'label': 'Sicherheit – Rettungshilfe - Anlaufstelle',
        'definition': 'Kontaktstellen der Institutionen, Organisationen oder Personen, an die man sich im Notfall wenden kann, um Hilfe oder Unterstützung zu bekommen (z. B. bei Feuer, Lebensgefahr, medizinischer Notlage)'
      },
      {
        'id': 'sicherheit/rettungshilfe/notfallnummer',
        'label': 'Sicherheit – Rettungshilfe - Notfallnummer',
        'definition': 'Öffentliche Orte, die mit Informationen zu Notfallnummern ausgestattet sind'
      },
      {
        'id': 'sicherheit/rettungshilfe/notinsel',
        'label': 'Sicherheit – Rettungshilfe - Notinsel',
        'definition': 'Standorte von Anlaufpunkten, die Kindern in Not im Rahmen des Projekts \'Notinsel\' als Zuflucht dienen'
      },
      {
        'id': 'sicherheit/rettungshilfe/waldrettungspunkt',
        'label': 'Sicherheit – Rettungshilfe - Waldrettungspunkt',
        'definition': 'Waldstandorte für die Notfallalarmierung'
      },
      {
        'id': 'sicherheit/zivilschutzUndKatastrophenschutz/kampfmittelfund',
        'label': 'Sicherheit – Zivilschutz und Katastrophenschutz - Kampfmittelfund',
        'definition': 'Daten zu Kampfmittelfunden und deren Beseitigung'
      },
      {
        'id': 'sicherheit/zivilschutzUndKatastrophenschutz/sirene',
        'label': 'Sicherheit – Zivilschutz und Katastrophenschutz - Sirene',
        'definition': 'Standorte der und Informationen zu Zivilschutzsirenen'
      },
      {
        'id': 'sonstiges',
        'label': 'Sonstiges',
        'definition': 'Unter Sonstiges werden Daten eingeordnet, die nicht in die übrigen Kategorien passen. Im Zuge von Weiterentwicklungen könnten aus diesen Datensätzen neue Kategorien gebildet werden.'
      },
      {
        'id': 'sonstiges/sonstiges',
        'label': 'Sonstiges',
        'definition': 'Unter Sonstiges werden Daten eingeordnet, die nicht in die übrigen Kategorien passen. Im Zuge von Weiterentwicklungen könnten aus diesen Datensätzen neue Kategorien gebildet werden.'
      },
      {
        'id': 'sozialeHilfe',
        'label': 'Soziale Hilfe',
        'definition': 'Daten zu Hilfen von öffentlichen Stellen in sozialen Notlagen'
      },
      {
        'id': 'sozialeHilfe/angebotUndBeratungsstelle',
        'label': 'Soziale Hilfe – Angebot und Beratungsstelle',
        'definition': 'Verzeichnis des öffentlichen Angebotes sozialer Hilfen bzw. der Beratungsstellen'
      },
      {
        'id': 'sozialeHilfe/behinderung/behindertenwohnheim',
        'label': 'Soziale Hilfe – Behinderung - Behindertenwohnheim',
        'definition': 'Einrichtungen für Menschen mit Behinderung'
      },
      {
        'id': 'sozialeHilfe/behinderung/menschenMitBehinderung',
        'label': 'Soziale Hilfe – Behinderung - Menschen mit Behinderung',
        'definition': 'Informationen zu Menschen mit Behinderung'
      },
      {
        'id': 'sozialeHilfe/bericht',
        'label': 'Soziale Hilfe – Bericht',
        'definition': 'Berichte über soziale Hilfestellungen'
      },
      {
        'id': 'sozialeHilfe/finanzielleUnterstuetzung/foerderung',
        'label': 'Soziale Hilfe – Finanzielle Unterstützung - Förderung',
        'definition': 'Finanzielle Unterstützungen im Rahmen der sozialen Hilfe'
      },
      {
        'id': 'sozialeHilfe/finanzielleUnterstuetzung/grundsicherung',
        'label': 'Soziale Hilfe – Finanzielle Unterstützung - Grundsicherung',
        'definition': 'Informationen zum Leistungsbezug der Grundsicherung'
      },
      {
        'id': 'sozialeHilfe/finanzielleUnterstuetzung/wohngeld',
        'label': 'Soziale Hilfe – Finanzielle Unterstützung - Wohngeld',
        'definition': 'Statistische Informationen zu Empfängerinnen und Empfängern von Wohngeld'
      },
      {
        'id': 'sozialeHilfe/flucht/asylbewerber',
        'label': 'Soziale Hilfe – Flucht - Asylbewerber',
        'definition': 'Statistische Informationen zu Leistungsbeziehenden nach dem Asylbewerberleistungsgesetz'
      },
      {
        'id': 'sozialeHilfe/flucht/fluechtlingsunterbringung',
        'label': 'Soziale Hilfe – Flucht - Flüchtlingsunterbringung',
        'definition': 'Entwicklung der Unterbringung von Flüchtlingen'
      },
      {
        'id': 'sozialeHilfe/flucht/fluechtlingszahl',
        'label': 'Soziale Hilfe – Flucht - Flüchtlingszahl',
        'definition': 'Zahl der Flüchtlinge'
      },
      {
        'id': 'sozialeHilfe/flucht/integration',
        'label': 'Soziale Hilfe – Flucht - Integration',
        'definition': 'Informationen zu den Angeboten der Flüchtlingshilfe'
      },
      {
        'id': 'sozialeHilfe/gefoerderterWohnungsbau',
        'label': 'Soziale Hilfe – Geförderter Wohnungsbau',
        'definition': 'Kennzahlen zu öffentlich geförderten Wohnungen'
      },
      {
        'id': 'sozialeHilfe/pflege',
        'label': 'Soziale Hilfe – Pflege',
        'definition': 'Informationen zu Pflegepersonal und Pflegeeinrichtungen'
      },
      {
        'id': 'staedtischesPersonal',
        'label': 'Städtisches Personal',
        'definition': 'Informationen zu städtischem Personal, wie etwa zu Stellenangeboten und -plänen sowie Bewerber- und Besoldungsstatistiken'
      },
      {
        'id': 'staedtischesPersonal/stellenausschreibung',
        'label': 'Städtisches Personal – Stellenausschreibung',
        'definition': 'Städtische Stellenangebote'
      },
      {
        'id': 'staedtischesPersonal/stellenplan',
        'label': 'Städtisches Personal – Stellenplan',
        'definition': 'Plan der Stellen im städtischen Dienst'
      },
      {
        'id': 'tourismus',
        'label': 'Tourismus',
        'definition': 'Informationen zum Städtetourismus'
      },
      {
        'id': 'tourismus/gaestezahl',
        'label': 'Tourismus – Gästezahl',
        'definition': 'Zahl der Gäste und Übernachtungen'
      },
      {
        'id': 'tourismus/sehenswuerdigkeit',
        'label': 'Tourismus – Sehenswürdigkeit',
        'definition': 'Touristenattraktionen'
      },
      {
        'id': 'tourismus/stadtfuehrung',
        'label': 'Tourismus – Stadtführung',
        'definition': 'Informationen zu Stadtrundgängen und touristischen Führungen'
      },
      {
        'id': 'tourismus/unterkunft/campingplatz',
        'label': 'Tourismus – Unterkunft - Campingplatz',
        'definition': 'Verzeichnis der Campingplätze'
      },
      {
        'id': 'tourismus/unterkunft/herberge',
        'label': 'Tourismus – Unterkunft - Herberge',
        'definition': 'Informationen zu Beherbergungen'
      },
      {
        'id': 'tourismus/unterkunft/hotel',
        'label': 'Tourismus – Unterkunft - Hotel',
        'definition': 'Standorte und Kontaktdetails der Hotelbetriebe'
      },
      {
        'id': 'tourismus/unterkunft/privatunterkunft',
        'label': 'Tourismus – Unterkunft - Privatunterkunft',
        'definition': 'Privatunterkünfte und Übernachtungsmöglichkeiten'
      },
      {
        'id': 'verkehr',
        'label': 'Verkehr',
        'definition': 'Angaben zu Fortbewegungsarten und Verkehrsinfrastruktur'
      },
      {
        'id': 'verkehr/ampelanlage',
        'label': 'Verkehr – Ampelanlage',
        'definition': 'Standorte der Ampelanlagen'
      },
      {
        'id': 'verkehr/flugverkehr/flugbewegung',
        'label': 'Verkehr – Flugverkehr - Flugbewegung',
        'definition': 'Flugbewegungen und Fluggastaufkommen'
      },
      {
        'id': 'verkehr/flugverkehr/flughafen',
        'label': 'Verkehr – Flugverkehr - Flughafen',
        'definition': 'Standorte und weitere Informationen zu Flughäfen'
      },
      {
        'id': 'verkehr/fussverkehr/fussgaengerzone',
        'label': 'Verkehr – Fußverkehr - Fußgängerzone',
        'definition': 'Verkehrsflächen, auf denen Fußgängerinnen und Fußgänger Vorrang oder ausschließliches Nutzungsrecht gegenüber anderen Verkehrsteilnehmerinnen und Verkehrsteilnehmern haben'
      },
      {
        'id': 'verkehr/fussverkehr/gehweg',
        'label': 'Verkehr – Fußverkehr - Gehweg',
        'definition': 'Bürgersteige'
      },
      {
        'id': 'verkehr/fussverkehr/laufstreckeUndWanderstrecke',
        'label': 'Verkehr – Fußverkehr - Laufstrecke und Wanderstrecke',
        'definition': 'Strecken zum Laufen und Wandern in Kommunen'
      },
      {
        'id': 'verkehr/kfz/Taxistand',
        'label': 'Verkehr – KFZ - Taxistand',
        'definition': 'Standorte der Taxihalteplätze'
      },
      {
        'id': 'verkehr/kfz/autobahn',
        'label': 'Verkehr – KFZ - Autobahn',
        'definition': 'Informationen zum Autobahn-Straßennetz'
      },
      {
        'id': 'verkehr/kfz/bussgeld',
        'label': 'Verkehr – KFZ - Bußgeld',
        'definition': 'Bußgelddaten'
      },
      {
        'id': 'verkehr/kfz/carsharing',
        'label': 'Verkehr – KFZ - Carsharing',
        'definition': 'Standorte und Fahrzeuge des Carsharing-Angebots'
      },
      {
        'id': 'verkehr/kfz/elektrotankstelle',
        'label': 'Verkehr – KFZ - Elektrotankstelle',
        'definition': 'E-Tankstellen zur Aufladung von Elektrofahrzeugen'
      },
      {
        'id': 'verkehr/kfz/fahrzeugzulassung',
        'label': 'Verkehr – KFZ - Fahrzeugzulassung',
        'definition': 'Statistiken zur Straßenverkehrszulassung von Fahrzeugen'
      },
      {
        'id': 'verkehr/kfz/messung',
        'label': 'Verkehr – KFZ - Messung',
        'definition': 'KFZ-Zählung und Geschwindigkeitsüberwachung'
      },
      {
        'id': 'verkehr/kfz/parkplatz',
        'label': 'Verkehr – KFZ - Parkplatz',
        'definition': 'Parkberechtigungen, Parkhäuser, Parkflächen'
      },
      {
        'id': 'verkehr/kfz/tankstelle',
        'label': 'Verkehr – KFZ - Tankstelle',
        'definition': 'Daten zu Tankstellen'
      },
      {
        'id': 'verkehr/oepnv/aufzugUndRolltreppe',
        'label': 'Verkehr – ÖPNV - Aufzug und Rolltreppe',
        'definition': 'Rolltreppen und Aufzüge im öffentlichen Personennahverkehr'
      },
      {
        'id': 'verkehr/oepnv/fahrgastzahl',
        'label': 'Verkehr – ÖPNV - Fahrgastzahl',
        'definition': 'Passagieraufkommen im kommunalen öffentlichen Personennahverkehr'
      },
      {
        'id': 'verkehr/oepnv/liniennetzSollfahrdatenEchtzeitdaten',
        'label': 'Verkehr – ÖPNV - Liniennetz Sollfahrdaten Echtzeitdaten',
        'definition': 'Netz der kommunalen Verkehrslinien bzw. Ist- und Sollfahrdaten'
      },
      {
        'id': 'verkehr/oepnv/vertriebsstelle',
        'label': 'Verkehr – ÖPNV - Vertriebsstelle',
        'definition': 'Standorte der Verkaufsstellen, Servicestellen und Fahrkartenautomaten im ÖPNV'
      },
      {
        'id': 'verkehr/radverkehr/abstellplatz',
        'label': 'Verkehr – Radverkehr - Abstellplatz',
        'definition': 'Standorte der Fahrradstellplätze'
      },
      {
        'id': 'verkehr/radverkehr/ladestation',
        'label': 'Verkehr – Radverkehr - Ladestation',
        'definition': 'E-Tankstellen zur Aufladung von Elektrofahrrädern'
      },
      {
        'id': 'verkehr/radverkehr/messung',
        'label': 'Verkehr – Radverkehr - Messung',
        'definition': 'Standorte und Messergebnisse der Radzählstellen'
      },
      {
        'id': 'verkehr/radverkehr/radwegUndRadroute',
        'label': 'Verkehr – Radverkehr - Radweg und Radroute',
        'definition': 'Informationen zu Radwegen und Radrouten'
      },
      {
        'id': 'verkehr/radverkehr/verleih',
        'label': 'Verkehr – Radverkehr - Verleih',
        'definition': 'Standorte der Fahrradmietsysteme'
      },
      {
        'id': 'verkehr/schiffsverkehrUndFaehrverkehr/anlegestelle',
        'label': 'Verkehr – Schiffsverkehr und Fährverkehr - Anlegestelle',
        'definition': 'Standorte der Schiffsanlegestellen und deren Belegung'
      },
      {
        'id': 'verkehr/schiffsverkehrUndFaehrverkehr/fracht',
        'label': 'Verkehr – Schiffsverkehr und Fährverkehr - Fracht',
        'definition': 'Güterumschlag'
      },
      {
        'id': 'verkehr/schiffsverkehrUndFaehrverkehr/passagier',
        'label': 'Verkehr – Schiffsverkehr und Fährverkehr - Passagier',
        'definition': 'Fahrgäste'
      },
      {
        'id': 'verkehr/sondernutzung',
        'label': 'Verkehr – Sondernutzung',
        'definition': 'Anträge auf Ausnahmegenehmigungen und Erlaubnisse im Straßenverkehr'
      },
      {
        'id': 'verkehr/unfall',
        'label': 'Verkehr – Unfall',
        'definition': 'Verkehrsunfälle, Verkehrsunfallentwicklung'
      },
      {
        'id': 'wetter',
        'label': 'Wetter',
        'definition': 'Wetterdaten'
      },
      {
        'id': 'wetter/hitze',
        'label': 'Wetter – Hitze',
        'definition': 'Hitzebelastung und Hitzeinseln im Stadtgebiet'
      },
      {
        'id': 'wetter/messung',
        'label': 'Wetter – Messung',
        'definition': 'Wettermessdaten'
      },
      {
        'id': 'wirtschaft',
        'label': 'Wirtschaft',
        'definition': 'Wirtschaftsdaten'
      },
      {
        'id': 'wirtschaft/arbeitslosigkeit',
        'label': 'Wirtschaft – Arbeitslosigkeit',
        'definition': 'Statistische Daten zu Arbeitslosigkeit'
      },
      {
        'id': 'wirtschaft/berufspendler',
        'label': 'Wirtschaft – Berufspendler',
        'definition': 'Infomationen zu Pendlerinnen und Pendlern, die regelmäßig zwischen Wohnort und Arbeitsplatz pendeln'
      },
      {
        'id': 'wirtschaft/beschaeftigung',
        'label': 'Wirtschaft – Beschäftigung',
        'definition': 'Statistische Daten zu Beschäftigung'
      },
      {
        'id': 'wirtschaft/beteiligungAnOeffentlicherWirtschaft/ausschreibungUndVergabe',
        'label': 'Wirtschaft – Beteiligung an Öffentlicher Wirtschaft - Ausschreibung und Vergabe',
        'definition': 'Vergaben und Ausschreibungen'
      },
      {
        'id': 'wirtschaft/beteiligungAnOeffentlicherWirtschaft/beteiligung',
        'label': 'Wirtschaft – Beteiligung an Öffentlicher Wirtschaft - Beteiligung',
        'definition': 'Anteile der Kommunen an Unternehmen der Daseinsvorsorge'
      },
      {
        'id': 'wirtschaft/bueroflaecheIndustrieflaecheGewerbeflaeche',
        'label': 'Wirtschaft – Bürofläche Industriefläche Gewerbefläche',
        'definition': 'Gewerblich genutzte Flächen'
      },
      {
        'id': 'wirtschaft/coworking',
        'label': 'Wirtschaft – Coworking',
        'definition': 'Gemeinsam genutzte bzw. geteilte Büroräumlichkeiten'
      },
      {
        'id': 'wirtschaft/dienstleistung/einzelhandel',
        'label': 'Wirtschaft – Dienstleistung - Einzelhandel',
        'definition': 'Einzelhandelsgeschäft'
      },
      {
        'id': 'wirtschaft/dienstleistung/handwerk',
        'label': 'Wirtschaft – Dienstleistung - Handwerk',
        'definition': 'Gewerbliche Tätigkeiten, die dem Handwerk zugeordnet werden (nicht industriell)'
      },
      {
        'id': 'wirtschaft/dienstleistung/postfiliale',
        'label': 'Wirtschaft – Dienstleistung - Postfiliale',
        'definition': 'Filialen der Postdienste'
      },
      {
        'id': 'wirtschaft/dienstleistung/weihnachtsmarkt',
        'label': 'Wirtschaft – Dienstleistung - Weihnachtsmarkt',
        'definition': 'Weihnachtsmärkte'
      },
      {
        'id': 'wirtschaft/dienstleistung/wochenmarkt',
        'label': 'Wirtschaft – Dienstleistung - Wochenmarkt',
        'definition': 'Regelmäßig stattfindende Märkte, besonders für Gemüse, Obst, Fleisch, Blumen'
      },
      {
        'id': 'wirtschaft/gewerbeanmeldung',
        'label': 'Wirtschaft – Gewerbeanmeldung',
        'definition': 'Anmeldung der Ausübung eines Gewerbes bei der Behörde'
      },
      {
        'id': 'wirtschaft/insolvenz',
        'label': 'Wirtschaft – Insolvenz',
        'definition': 'Unternehmensinsolvenzen'
      },
      {
        'id': 'wirtschaft/wirtschaftsfoerderung',
        'label': 'Wirtschaft – Wirtschaftsförderung',
        'definition': 'Förderung der Wirtschaft durch Kommunen durch finanzielle oder andere Zuwendungen'
      },
      {
        'id': 'wirtschaft/wirtschaftsstandort',
        'label': 'Wirtschaft – Wirtschaftsstandort',
        'definition': 'Wirtschaftsrahmenbedingungen in einem bestimmten Gebiet'
      }
    ]

def render_sample_record(value, **attrs):
    # TODO: that's obviously super inefficient to compute this every time...
    record_dict = {sample_record['id']: sample_record['label'] for sample_record in sample_record_select_options()}
    if value in record_dict:
      return link_to(record_dict[value], f'https://musterdatenkatalog.de/def/musterdatensatz/{value}', **attrs)
    return ""

def render_govdata_example_link(value):
    govdata_sparql_link = f"https://www.govdata.de/web/guest/sparql-assistent#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fdatensatz%0A%20%20%20%20dct%3Areferences%20%3Chttps%3A%2F%2Fmusterdatenkatalog.de%2Fdef%2Fmusterdatensatz%2F{value}%3E%20%3B%0A%20%20%20%20dct%3Atitle%20%3Ftitle%20%3B%0A%20%20.%0A%7D%20&endpoint=https%3A%2F%2Fwww.govdata.de%2Fsparql&requestMethod=GET&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=text%2Fturtle%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bxml%2C*%2F*%3Bq%3D0.9&outputFormat=table"
    return link_to("Beispiele bei GovData.de", govdata_sparql_link)

def hvd_category_select_options() -> list:
    return [
        { 'id': '', 'label': 'Keine' },
        { 'id': 'c_dd313021', 'label': 'Erdbeobachtung und Umwelt' },
        { 'id': 'c_38933a65', 'label': 'Erdbeobachtung und Umwelt / Abfall' },
        { 'id': 'c_af646f5b', 'label': 'Erdbeobachtung und Umwelt / Bewirtschaftungsgebiete/Schutzgebiete/geregelte Gebiete und Berichterstattungseinheiten' },
        { 'id': 'c_c873f344', 'label': 'Erdbeobachtung und Umwelt / Biogeografische Regionen' },
        { 'id': 'c_87a129d9', 'label': 'Erdbeobachtung und Umwelt / Boden' },
        { 'id': 'c_b21e1296', 'label': 'Erdbeobachtung und Umwelt / Bodenbedeckung' },
        { 'id': 'c_ad9ae929', 'label': 'Erdbeobachtung und Umwelt / Bodennutzung' },
        { 'id': 'c_4ba9548e', 'label': 'Erdbeobachtung und Umwelt / Emissionen' },
        { 'id': 'c_b7de66cd', 'label': 'Erdbeobachtung und Umwelt / Energiequellen' },
        { 'id': 'c_b7f6a4f3', 'label': 'Erdbeobachtung und Umwelt / Erhaltung der Natur und der biologischen Vielfalt' },
        { 'id': 'c_63be22bd', 'label': 'Erdbeobachtung und Umwelt / Gebiete mit naturbedingten Risiken' },
        { 'id': 'c_e3f55603', 'label': 'Erdbeobachtung und Umwelt / Geologie' },
        { 'id': 'c_06b1eec4', 'label': 'Erdbeobachtung und Umwelt / Gewässernetz' },
        { 'id': 'c_4d63300b', 'label': 'Erdbeobachtung und Umwelt / Horizontale Rechtsvorschriften' },
        { 'id': 'c_315692ad', 'label': 'Erdbeobachtung und Umwelt / Höhe' },
        { 'id': 'c_59e64dd4', 'label': 'Erdbeobachtung und Umwelt / Klima' },
        { 'id': 'c_c3919aec', 'label': 'Erdbeobachtung und Umwelt / Lebensräume und Biotope' },
        { 'id': 'c_63b37dd4', 'label': 'Erdbeobachtung und Umwelt / Luft' },
        { 'id': 'c_e4358335', 'label': 'Erdbeobachtung und Umwelt / Lärm' },
        { 'id': 'c_f399050e', 'label': 'Erdbeobachtung und Umwelt / Meeresregionen' },
        { 'id': 'c_4dd389c5', 'label': 'Erdbeobachtung und Umwelt / Mineralische Bodenschätze' },
        { 'id': 'c_91185a85', 'label': 'Erdbeobachtung und Umwelt / Orthofotografie' },
        { 'id': 'c_b40e6d46', 'label': 'Erdbeobachtung und Umwelt / Ozeanografisch-geografische Kennwerte' },
        { 'id': 'c_59c93ba5', 'label': 'Erdbeobachtung und Umwelt / Produktions- und Industrieanlagen' },
        { 'id': 'c_83aa10a6', 'label': 'Erdbeobachtung und Umwelt / Schutzgebiete' },
        { 'id': 'c_7b8fbb64', 'label': 'Erdbeobachtung und Umwelt / Umweltüberwachungseinrichtungen' },
        { 'id': 'c_793164b6', 'label': 'Erdbeobachtung und Umwelt / Verteilung der Arten' },
        { 'id': 'c_43f88346', 'label': 'Erdbeobachtung und Umwelt / Wasser' },
        { 'id': 'c_ac64a52d', 'label': 'Georaum' },
        { 'id': 'c_c3de25e4', 'label': 'Georaum / Adressen' },
        { 'id': 'c_6a3f6896', 'label': 'Georaum / Flurstücke/Grundstücke (Katasterparzellen)' },
        { 'id': 'c_60182062', 'label': 'Georaum / Gebäude' },
        { 'id': 'c_6c2bb82d', 'label': 'Georaum / Geografische Bezeichnungen' },
        { 'id': 'c_642643e6', 'label': 'Georaum / Landwirtschaftliche Parzellen' },
        { 'id': 'c_fbd2fc3f', 'label': 'Georaum / Referenzparzellen' },
        { 'id': 'c_9427236f', 'label': 'Georaum / Verwaltungseinheiten' },
        { 'id': 'c_164e0bf5', 'label': 'Meteorologie' },
        { 'id': 'c_3af3368c', 'label': 'Meteorologie / Beobachtungsmessdaten von Wetterstationen' },
        { 'id': 'c_36807466', 'label': 'Meteorologie / Klimadaten: validierte Beobachtungen' },
        { 'id': 'c_13e3cf16', 'label': 'Meteorologie / NWP-Modelldaten' },
        { 'id': 'c_d13a4420', 'label': 'Meteorologie / Radardaten' },
        { 'id': 'c_be47b010', 'label': 'Meteorologie / Wetterwarnungen' },
        { 'id': 'c_b79e35eb', 'label': 'Mobilität' },
        { 'id': 'c_b151a0ba', 'label': 'Mobilität / Binnenschifffahrtsdatensätze' },
        { 'id': 'c_f6886b00', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Beschränkungen infolge von Hochwasser und Eis' },
        { 'id': 'c_664c9e5a', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Fahrwasser-/Fahrrinnengrenzen' },
        { 'id': 'c_f76b01e6', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Fahrwassermerkmale' },
        { 'id': 'c_e5f69a04', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Gegenwärtige und zukünftige Wasserstände an den Pegeln' },
        { 'id': 'c_25f43866', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Höhe der Abgaben für die Wasserstraßen-Infrastruktur' },
        { 'id': 'c_99bc517f', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Isolierte Gefahrenstellen im Fahrwasser/in der Fahrrinne unter und über Wasser' },
        { 'id': 'c_593bc53d', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Kurzfristige Änderungen bei den Schifffahrtszeichen' },
        { 'id': 'c_66b946cb', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Kurzfristige Änderungen der Betriebszeiten von Schleusen und Brücken' },
        { 'id': 'c_3e8e3bf7', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Lage und Merkmale von Häfen und Umschlagstellen' },
        { 'id': 'c_407951ff', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Lage von Häfen und Umschlagstellen' },
        { 'id': 'c_fa2a1c3a', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Langzeitbehinderungen im Fahrweg und Zuverlässigkeit' },
        { 'id': 'c_298ffb73', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Links zu den externen xml-Dateien mit Betriebszeiten einschränkender Infrastrukturen' },
        { 'id': 'c_9cbe4435', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Liste der Navigationshilfen und Verkehrszeichen' },
        { 'id': 'c_03ba8d92', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Normale Betriebszeiten der Schleusen und Brücken' },
        { 'id': 'c_b24028d7', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Offizielle Schifffahrtszeichen (z. B. Tonnen, Baken, Leuchtzeichen, Tafelzeichen)' },
        { 'id': 'c_1e787364', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Referenzdaten für die schifffahrtsrelevanten Pegel' },
        { 'id': 'c_7e19ef26', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Sonstige physische Beschränkungen auf Wasserstraßen' },
        { 'id': 'c_fef208ab', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Tiefenlinien in der Fahrrinne' },
        { 'id': 'c_1226dc1a', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Ufer der Wasserstraße bei Mittelwasser' },
        { 'id': 'c_bc8941d9', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Uferbefestigung' },
        { 'id': 'c_883d0205', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Umrisse der Schleusen und Wehre' },
        { 'id': 'c_2037ada4', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Vorschriften und Empfehlungen für die Schifffahrt' },
        { 'id': 'c_b121e2f6', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Vorübergehende Hindernisse im Fahrwasser' },
        { 'id': 'c_c19af83a', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Wasserstraßenachse mit Kilometerangabe' },
        { 'id': 'c_e50004c6', 'label': 'Mobilität / Binnenschifffahrtsdatensätze / Zustand der Flüsse, Kanäle, Schleusen und Brücken' },
        { 'id': 'c_4b74ea13', 'label': 'Mobilität / Verkehrsnetze' },
        { 'id': 'c_e1da4e07', 'label': 'Statistik' },
        { 'id': 'c_04bf94a3', 'label': 'Statistik / Armut' },
        { 'id': 'c_4ac557e7', 'label': 'Statistik / Ausgaben und Einnahmen des Staates' },
        { 'id': 'c_f2b50efd', 'label': 'Statistik / Bevölkerung' },
        { 'id': 'c_317b9493', 'label': 'Statistik / Bevölkerung, Fertilität, Mortalität' },
        { 'id': 'c_fd4e881c', 'label': 'Statistik / Erwerbslosigkeit' },
        { 'id': 'c_a2c6dcd8', 'label': 'Statistik / Erwerbstätigkeit' },
        { 'id': 'c_6a7250c1', 'label': 'Statistik / Fertilität' },
        { 'id': 'c_c0022235', 'label': 'Statistik / Harmonisierte Verbraucherpreisindizes' },
        { 'id': 'c_2aed31f9', 'label': 'Statistik / Industrieller Erzeugerpreisindex – Aufschlüsselung nach Tätigkeit' },
        { 'id': 'c_34abf8c1', 'label': 'Statistik / Industrieproduktion' },
        { 'id': 'c_dd8f4797', 'label': 'Statistik / Konsolidierte Bruttoverschuldung des Staates' },
        { 'id': 'c_424bb0b4', 'label': 'Statistik / Laufende Gesundheitsausgaben' },
        { 'id': 'c_4acb6bf3', 'label': 'Statistik / Mortalität' },
        { 'id': 'c_23385471', 'label': 'Statistik / Potenzielle Arbeitskräfte' },
        { 'id': 'c_20cd11bb', 'label': 'Statistik / Statistik des internationalen Warenverkehrs der EU – Ausfuhren und Einfuhren Aufschlüsselung gleichzeitig nach Partnern, Produkten und Warenströmen' },
        { 'id': 'c_a3767648', 'label': 'Statistik / Tourismusströme in Europa' },
        { 'id': 'c_92874eb2', 'label': 'Statistik / Umweltgesamtrechnungen und -statistiken' },
        { 'id': 'c_a8b937c4', 'label': 'Statistik / Ungleichheit' },
        { 'id': 'c_a49ec591', 'label': 'Statistik / Verkaufsmengen nach Tätigkeit' },
        { 'id': 'c_b72b721f', 'label': 'Statistik / Volkswirtschaftliche Gesamtrechnungen – BIP-Hauptaggregate' },
        { 'id': 'c_95da87c7', 'label': 'Statistik / Volkswirtschaftliche Gesamtrechnungen – Schlüsselindikatoren für Kapitalgesellschaften' },
        { 'id': 'c_59627af3', 'label': 'Statistik / Volkswirtschaftliche Gesamtrechnungen – Schlüsselindikatoren für private Haushalte' },
        { 'id': 'c_a9135398', 'label': 'Unternehmen und Eigentümerschaft von Unternehmen' },
        { 'id': 'c_56a1bf47', 'label': 'Unternehmen und Eigentümerschaft von Unternehmen / Grundlegende Angaben zum Unternehmen: Schlüsselattribute' },
        { 'id': 'c_8f0fac04', 'label': 'Unternehmen und Eigentümerschaft von Unternehmen / Unternehmensunterlagen und -abschlüsse' },
    ]

def render_hvd_category(value: str, **attrs) -> str:
    # TODO: that's obviously super inefficient to compute this every time...
    hvd_dict = {hvd_category['id']: hvd_category['label'] for hvd_category in hvd_category_select_options()}
    if value in hvd_dict:
      return link_to(hvd_dict[value], f'http://data.europa.eu/bna/{value}', **attrs)
    return ""

def author_uri_select_options() -> list:
    return [
      {'id': 'org_e8a44cc6-5562-554d-b1cc-498499725fc0', 'label': 'Amt für Statistik Berlin-Brandenburg'},
      {'id': 'org_a02b149b-d470-5b32-a51e-58cde32a902e', 'label': 'BerlinOnline GmbH'},
      {'id': 'org_d3653f97-876d-5a01-a789-7056db7b5402', 'label': 'Berliner Feuerwehr'},
      {'id': 'org_86a7ec73-0509-5892-b4c5-08e2849c9f86', 'label': 'Berliner Forsten'},
      {'id': 'org_6d24ed7d-82ef-557e-b353-c62f3619ebda', 'label': 'Berliner Stadtreinigung (BSR)'},
      {'id': 'org_9871655c-38c3-5e72-a454-6dc660cf92e8', 'label': 'Berliner Wasserbetriebe'},
      {'id': 'org_5a62e5a6-027c-591b-9478-64f21a985d1f', 'label': 'Bezirksamt Charlottenburg-Wilmersdorf'},
      {'id': 'org_1d65d3ff-4ec0-5c38-a78b-9c19ed5cd4a1', 'label': 'Bezirksamt Friedrichshain-Kreuzberg'},
      {'id': 'org_311697a3-e8e7-5cee-be46-4e967bb6d000', 'label': 'Bezirksamt Lichtenberg'},
      {'id': 'org_0f98664c-7984-5e3a-b69c-6d00d2ffc7d8', 'label': 'Bezirksamt Marzahn-Hellersdorf'},
      {'id': 'org_7ab3a225-dfe2-5ebf-8fb9-7013d3c8e7a2', 'label': 'Bezirksamt Mitte'},
      {'id': 'org_ba6882fd-d241-56ba-be3d-32954693277f', 'label': 'Bezirksamt Neukölln'},
      {'id': 'org_b8fc6e76-216e-53da-afe9-82df40eaef16', 'label': 'Bezirksamt Pankow'},
      {'id': 'org_2d6abcbf-92af-5307-b643-8d828da74713', 'label': 'Bezirksamt Reinickendorf'},
      {'id': 'org_2145c6c3-c54e-535f-bff9-afa331d5a393', 'label': 'Bezirksamt Spandau'},
      {'id': 'org_aad33c44-2637-53c4-a579-bc730515c3dc', 'label': 'Bezirksamt Steglitz-Zehlendorf'},
      {'id': 'org_4e981fee-ab6a-5806-9822-2387e45322e7', 'label': 'Bezirksamt Tempelhof-Schöneberg'},
      {'id': 'org_e140c773-20ee-5372-8e5d-1fdc9031a9ec', 'label': 'Bezirksamt Treptow-Köpenick'},
      {'id': 'org_d1ee1260-8cf0-560f-a495-6941438f45da', 'label': 'Industrie- und Handelskammer zu Berlin'},
      {'id': 'org_f49062d8-5c1f-5ac9-b932-a9e2efd62170', 'label': 'Landesamt für Bürger- und Ordnungsangelegenheiten'},
      {'id': 'org_012340ce-1c0e-508d-99be-bb27c9a8c095', 'label': 'Landesamt für Gesundheit und Soziales'},
      {'id': 'org_4ec63f8b-7b9b-5aec-84f4-81924235342d', 'label': 'Polizei Berlin'},
      {'id': 'org_53dfb317-5e72-5dc6-942c-fd29972e909a', 'label': 'Senatsverwaltung für Arbeit, Soziales, Gleichstellung, Integration, Vielfalt und Antidiskriminierung'},
      {'id': 'org_f190754b-cdc9-5483-9ab0-18512e393e53', 'label': 'SenASGIVA – Abteilung I – Integration und Migration'},
      {'id': 'org_f995b52f-54a7-5c0c-9956-a364ee4bcdcf', 'label': 'SenASGIVA – Abteilung II – Arbeit und Berufliche Bildung'},
      {'id': 'org_45f3e63b-c5bd-5b1f-9c13-3a68ff9a3600', 'label': 'SenASGIVA – Abteilung III – Soziales'},
      {'id': 'org_ebceecbd-8da7-5141-8c87-57eb596caab4', 'label': 'SenASGIVA – Abteilung IV – Antidiskriminierung und Vielfalt'},
      {'id': 'org_bb0fc996-ad62-5048-a64d-fb54b48b79a4', 'label': 'SenASGIVA – Abteilung V – Frauen und Gleichstellung'},
      {'id': 'org_57a6dd31-b1d3-5fc2-b73a-0cc8a638d9ce', 'label': 'Senatsverwaltung für Bildung, Jugend und Familie'},
      {'id': 'org_6222a6ad-a641-53d3-89a2-b235e2cbc42f', 'label': 'SenBFJ – Abteilung I – Unterstützung und Beratung der Schulen, operative Schulaufsicht, Schulpsychologie, Personalmanage- ment, Bildungsstatistik und Prognose'},
      {'id': 'org_b7ec616e-b5a7-57f0-8bda-fe3463c86411', 'label': 'SenBFJ – Abteilung II – Grundsatzangelegenheiten und Recht des Bildungswesens; allgemein bildende Schulen; Lehrkräftebildung'},
      {'id': 'org_d138a877-1f5e-561d-98b5-3608d0a62761', 'label': 'SenBFJ – Abteilung III – Jugend und Kinderschutz'},
      {'id': 'org_e63e6f20-60e0-527e-97e8-06939cb5f8df', 'label': 'SenBFJ – Abteilung IV – Schulische Berufliche Bildung; Zentralverwaltete Schulen, Europäische und Internationale Angelegenheiten'},
      {'id': 'org_39caa39a-6cc6-5688-a2c6-a01535bb68ef', 'label': 'SenBFJ – Abteilung V – Familie und frühkindliche Bildung'},
      {'id': 'org_cc609d28-8df8-5860-b08f-712749621968', 'label': 'SenBFJ – Abteilung VI – Schulentwicklungsplanung und Schulinfrastruktur im Land Berlin'},
      {'id': 'org_387580ee-5ee1-5071-88f7-c6e22e3bb2e9', 'label': 'SenBFJ – Abteilung VII – Schule in der digitalen Welt'},
      {'id': 'org_5ae6cac5-817e-57a3-9b46-c697dfbba6cd', 'label': 'Senatsverwaltung für Finanzen'},
      {'id': 'org_5fc5695e-d720-59e5-8c4b-6a5651d0c332', 'label': 'SenFin – Abteilung I – Vermögen und Beteiligungen'},
      {'id': 'org_3794220b-52b3-5735-8eb3-b636d8ecebb9', 'label': 'SenFin – Abteilung II – Finanzpolitik und Haushalt'},
      {'id': 'org_34392488-463d-54c4-891d-5928b2f88e7e', 'label': 'SenFin – Abteilung III – Angelegenheiten der Steuerverwaltung'},
      {'id': 'org_77fecfe8-14e5-5702-a380-79115515df11', 'label': 'SenFin – Abteilung IV – Landespersonal'},
      {'id': 'org_26ab9744-b1f8-5766-b4db-0de2e39c5921', 'label': 'Senatsverwaltung für Inneres und Sport'},
      {'id': 'org_05a92a03-d5e1-5aef-a21b-253ba4c12d81', 'label': 'SenInn – Abteilung I – Staats-und Verwaltungsrecht'},
      {'id': 'org_8e2f66f8-b4d5-51ac-9f5b-3904e14b0696', 'label': 'SenInn – Abteilung II – Verfassungsschutz'},
      {'id': 'org_3b7d8f6f-c25f-545a-b2cf-4c95ef15f29c', 'label': 'SenInn – Abteilung III – Öffentliche Sicherheit und Ordnung'},
      {'id': 'org_53708410-faf3-5fb9-85a4-b0b9ba50e9bc', 'label': 'SenInn – Abteilung IV – Sport'},
      {'id': 'org_e2987a2c-731e-5f43-91e4-639c646ea480', 'label': 'Senatsverwaltung für Justiz und Verbraucherschutz'},
      {'id': 'org_048463ab-b58c-5723-b531-ae1863d68a0b', 'label': 'SenJustV – Abteilung I – Innere Dienste, Sozialberatung der Berliner Justiz (organisatorisch), Justiz und Gesellschaft - Justiz in der vielfältigen Gesellschaft, Justizielle Opferhilfe und Zentrale Anlaufstelle für Betroffene von Terroranschlägen und deren Angehörigen, Baureferat'},
      {'id': 'org_8672d1a6-ab17-5988-8dd9-a29192f1dbc2', 'label': 'SenJustV – Abteilung II – Zivilrecht, öffentliches Recht, Angelegenheiten der Informations- und Kommunikationstechnik der Gerichte und Strafverfolgungsbehörden, Stiftungsaufsicht'},
      {'id': 'org_5d2358c4-275a-5332-a5a3-fd805884a6a8', 'label': 'SenJustV – Abteilung III – Justizvollzug, Gnadenwesen, Soziale Dienste der Justiz - Gerichts- und Bewährungshilfe, Strafrecht, Strafverfahrensrecht, Strafvollstreckung'},
      {'id': 'org_f34efc6b-bb66-5917-bc34-9a090cadb709', 'label': 'SenJustV – Abteilung IV – Gemeinsames Juristisches Prüfungsamt der Länder Berlin und Brandenburg, Juristische Prüfungen, Aus- und. Fortbildung in der Rechtspflege'},
      {'id': 'org_cb7623d8-3c74-565d-b92d-39fbda9bfa07', 'label': 'SenJustV – Abteilung V – Verbraucherschutz'},
      {'id': 'org_4eff6ca7-69b6-5616-a112-16937f5bbcb8', 'label': 'Senatsverwaltung für Kultur und Gesellschaftlichen Zusammenhalt'},
      {'id': 'org_f9262704-7bba-5da4-a36b-1bdf30acec7d', 'label': 'SenKultGZ – Abteilung I – Kultur'},
      {'id': 'org_97219240-ec15-5973-bb68-3e366dd2f4be', 'label': 'SenKultGZ – Abteilung II – Engagement- und Demokratieförderung, Beauftragter für Kirchen, Religions- und Weltanschauungsgemeinschaften'},
      {'id': 'org_ed497d1d-bc70-5e4a-944d-abbe7d253b63', 'label': 'Senatsverwaltung für Mobilität, Verkehr, Klimaschutz und Umwelt'},
      {'id': 'org_68794a8e-7bc4-59d5-89c4-fa8b953467e7', 'label': 'SenMVKU – Abteilung I – Umwelt- und Klimaschutzpolitik, Kreislaufwirtschaft und Immissionsschutz'},
      {'id': 'org_8f366820-b8a5-57b6-8335-76dfc141cc78', 'label': 'SenMVKU – Abteilung II – Integrativer Umweltschutz'},
      {'id': 'org_80390e27-c7d5-592b-82be-d3eb7574580c', 'label': 'SenMVKU – Abteilung III – Naturschutz und Stadtgrün'},
      {'id': 'org_8e49bdaa-7b27-5d06-9579-ef9e829f3c29', 'label': 'SenMVKU – Abteilung IV – Mobilität'},
      {'id': 'org_6ed022a3-88ce-5249-82c5-4747589fd9f2', 'label': 'SenMVKU – Abteilung V – Tiefbau'},
      {'id': 'org_2bb6adf9-674f-5af4-a642-11e277e0d795', 'label': 'SenMVKU – Abteilung VI – Verkehrsmanagement'},
      {'id': 'org_4af7b849-8767-5dc1-b244-4de42772cfe8', 'label': 'Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen'},
      {'id': 'org_39a71ccf-6b45-5e66-9cd1-e6f4a342db12', 'label': 'SenSBW – Abteilung I – Stadtplanung'},
      {'id': 'org_94db7d7c-3911-566f-9ce0-094fede59651', 'label': 'SenSBW – Abteilung II – Städtebau und Projekte'},
      {'id': 'org_f9249be0-fa88-5b4b-b6d4-b72be17ff64e', 'label': 'SenSBW – Abteilung III – Geoinformation'},
      {'id': 'org_9420ce0e-0c0d-567e-8160-d5d3957a4923', 'label': 'SenSBW – Abteilung IV – Wohnen und Stadterneuerung'},
      {'id': 'org_8c343579-25ee-5a7d-ab90-a8410a6953ab', 'label': 'SenSBW – Abteilung V – Hochbau'},
      {'id': 'org_ca09e19e-dcb6-5e9f-b789-ed1df60e41eb', 'label': 'SenSBW – Abteilung VI – Ministerielle Angelegenheiten des Bauens, Grundsatz und Recht'},
      {'id': 'org_f05f949d-c390-53fa-bc4f-5ab67da59d89', 'label': 'Senatsverwaltung für Wirtschaft, Energie und Betriebe'},
      {'id': 'org_8d7e907b-8a07-5443-b7ec-f46dd9300d07', 'label': 'SenSBW – Abteilung II – Wirtschaftspolitik und Wirtschaftsordnung'},
      {'id': 'org_1f6e40be-5c12-56f7-8fcb-787df0079dfe', 'label': 'SenSBW – Abteilung III – Energie, Digitalisierung, Innovation'},
      {'id': 'org_86fe495f-9cf1-5e53-a33e-e461a154924a', 'label': 'SenSBW – Abteilung IV – Betriebe und Strukturpolitik'},
      {'id': 'org_b9716bdb-0680-5807-b7be-b5fc45a0b89b', 'label': 'Senatsverwaltung für Wissenschaft, Gesundheit und Pflege'},
      {'id': 'org_0e1b0ac2-407f-520f-b59b-9c2fa67271c2', 'label': 'SenWGP – Abteilung I – Gesundheit'},
      {'id': 'org_062b66ef-35b8-5be0-bee0-090a345d821a', 'label': 'SenWGP – Abteilung II – Pflege'},
      {'id': 'org_5995cccc-4e1c-5323-abbe-0ea5e4e03c55', 'label': 'VBB - Verkehrsverbund Berlin-Brandenburg GmbH'}
    ]


def render_author_uri(value: str, **attrs) -> str:
    # TODO: that's obviously super inefficient to compute this every time...
    author_uri_dict = {author_uri['id']: author_uri['label'] for author_uri in author_uri_select_options()}
    if value in author_uri_dict:
      return link_to(author_uri_dict[value], f'https://berlin.github.io/lod-core-organigram/{value}', **attrs)
    return ""

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

def org_is_external(org: str) -> bool:
    org = helpers.get_organization(org)
    extras = org.get('extras', [])
    for extra in extras:
        if extra['key'] == 'external' and extra['value'] == 'true':
          return True
    return False