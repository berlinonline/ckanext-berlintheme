# coding: utf-8

import logging
from ckan.lib.helpers import link_to
import ckan.logic as logic
import ckan.model as model
from ckan.common import c, config
from ckanext.berlin_dataset_schema.schema import Schema
import ckan.plugins.toolkit as toolkit

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
      {
        "id": "abfallentsorgung",
        "label": "Abfallentsorgung",
        "definition": "Beseitigung von Müll"
      },
      {
        "id": "abfallentsorgung/abfallkalender",
        "label": "Abfallentsorgung – Abfallkalender",
        "definition": "Auflistung der Müllabfuhrtermine nach Abfallkategorie und Ort"
      },
      {
        "id": "abfallentsorgung/abfallmenge",
        "label": "Abfallentsorgung – Abfallmenge",
        "definition": "Menge des entsorgten Mülls nach unterschiedlichen Abfallarten"
      },
      {
        "id": "abfallentsorgung/abgabestelle",
        "label": "Abfallentsorgung – Abgabestelle",
        "definition": "Ort, an dem bestimmte Müllkategorien abgegeben werden können"
      },
      {
        "id": "abfallentsorgung/container",
        "label": "Abfallentsorgung – Container",
        "definition": "Standorte der Großraumbehälter zur Sammlung, Zwischenlagerung und zum Transport von Müll"
      },
      {
        "id": "abfallentsorgung/entwaesserung",
        "label": "Abfallentsorgung – Entwässerung",
        "definition": "Statistiken zum Abführen von [Ab]wasser durch künstliche und natürliche Einrichtungen"
      },
      {
        "id": "abfallentsorgung/muellgebuehr",
        "label": "Abfallentsorgung – Müllgebühr",
        "definition": "Entgelt für die Abfallentsorgung"
      },
      {
        "id": "abfallentsorgung/strassenreinigung",
        "label": "Abfallentsorgung – Straßenreinigung",
        "definition": "Reinigung öffentlicher Straßen und Plätze"
      },
      {
        "id": "bau",
        "label": "Bau",
        "definition": "Bauen, Errichten, Herstellen"
      },
      {
        "id": "bau/baufertigstellung",
        "label": "Bau – Baufertigstellung",
        "definition": "Bauvorhaben, deren Bauarbeiten weitgehend abgeschlossen sind"
      },
      {
        "id": "bau/baugenehmigung",
        "label": "Bau – Baugenehmigung",
        "definition": "Bauaufsichtsbehördlich erteilte Genehmigung zur Errichtung, Änderung oder Beseitigung eines Baus"
      },
      {
        "id": "bau/baustelle",
        "label": "Bau – Baustelle",
        "definition": "Orte, an denen Bauwerke errichtet, umgebaut oder abgerissen werden"
      },
      {
        "id": "bau/bauvorhaben",
        "label": "Bau – Bauvorhaben",
        "definition": "Gesamter Planungs- und Arbeitsprozess zum Herstellen oder Verändern eines Bauobjekts"
      },
      {
        "id": "bau/brunnen",
        "label": "Bau – Brunnen",
        "definition": "Brunnen und Teichfontänen"
      },
      {
        "id": "bau/grundstuecksbewertung",
        "label": "Bau – Grundstücksbewertung",
        "definition": "Wertermittlung für bebaute und unbebaute Grundstücke und grundstücksgleiche Rechte (Immobilien)"
      },
      {
        "id": "bau/tiefbau",
        "label": "Bau – Tiefbau",
        "definition": "Angaben zum Tätigkeitsbereich der Tiefbauämter"
      },
      {
        "id": "bau/wohnungsbestand",
        "label": "Bau – Wohnungsbestand",
        "definition": "Wohngebäudebestand, Gesamtzahl der in einem Gebiet an einem Stichtag vorhandenen Häuser und Wohnungen"
      },
      {
        "id": "bevoelkerungsstruktur",
        "label": "Bevölkerungsstruktur",
        "definition": "Zusammensetzung einer Bevölkerung nach bestimmten Merkmalen, die deren Charakteristika beschreiben"
      },
      {
        "id": "bevoelkerungsstruktur/demografiebericht",
        "label": "Bevölkerungsstruktur – Demografiebericht",
        "definition": "Bericht, der die demografische Entwicklung für Kommunen darstellt"
      },
      {
        "id": "bevoelkerungsstruktur/einwohnerzahl",
        "label": "Bevölkerungsstruktur – Einwohnerzahl",
        "definition": "Gesamtzahl der Einwohnerinnen und Einwohner"
      },
      {
        "id": "bevoelkerungsstruktur/haushaltszusammensetzung",
        "label": "Bevölkerungsstruktur – Haushaltszusammensetzung",
        "definition": "Personen, die in einer gemeinsamen Wohnung leben"
      },
      {
        "id": "bevoelkerungsstruktur/migrationshintergrund",
        "label": "Bevölkerungsstruktur – Migrationshintergrund",
        "definition": "Daten zur Bevölkerungszusammensetzung im Hinblick auf den Faktor 'Migrationshintergrund'"
      },
      {
        "id": "bevoelkerungsstruktur/religionszugehoerigkeit",
        "label": "Bevölkerungsstruktur – Religionszugehörigkeit",
        "definition": "Zugehörigkeit einer Person zu einer bestimmten Religionsgemeinschaft"
      },
      {
        "id": "bevoelkerungsstruktur/staatsangehoerigkeit",
        "label": "Bevölkerungsstruktur – Staatsangehörigkeit",
        "definition": "Angaben zur Staatsangehörigkeit der Bevölkerung"
      },
      {
        "id": "bevoelkerungsstruktur/vorname",
        "label": "Bevölkerungsstruktur – Vorname",
        "definition": "Statistiken zu vergebenen Vornamen"
      },
      {
        "id": "bildung",
        "label": "Bildung",
        "definition": "Vermittlung von Fertigkeiten und Wissen durch eine dazu befugte Einrichtung, beispielsweise eine staatliche Schule, eine Hochschule oder ein privates Unternehmen"
      },
      {
        "id": "bildung/ausbildung",
        "label": "Bildung – Ausbildung",
        "definition": "Ausbildungseinrichtungen"
      },
      {
        "id": "bildung/bibliothek/ausleihe",
        "label": "Bildung – Bibliothek - Ausleihe",
        "definition": "Verliehene Bibliotheksmedien"
      },
      {
        "id": "bildung/bibliothek/bestand",
        "label": "Bildung – Bibliothek - Bestand",
        "definition": "Gesamtheit der in Bibliotheken gesammelten Publikationen"
      },
      {
        "id": "bildung/bibliothek/besucherzahl",
        "label": "Bildung – Bibliothek - Besucherzahl",
        "definition": "Anzahl der Besucherinnen und Besucher von Bibliotheken"
      },
      {
        "id": "bildung/bibliothek/budget",
        "label": "Bildung – Bibliothek - Budget",
        "definition": "Finanzpläne von Bibliotheken"
      },
      {
        "id": "bildung/bibliothek/standort",
        "label": "Bildung – Bibliothek - Standort",
        "definition": "Standorte von Bibliotheken"
      },
      {
        "id": "bildung/hochschule/standort",
        "label": "Bildung – Hochschule - Standort",
        "definition": "Standorte von Hochschulen"
      },
      {
        "id": "bildung/hochschule/studentenwohnheim",
        "label": "Bildung – Hochschule - Studentenwohnheim",
        "definition": "Unterkünfte für Studierende"
      },
      {
        "id": "bildung/hochschule/studierendenzahl",
        "label": "Bildung – Hochschule - Studierendenzahl",
        "definition": "Anzahl der Studierenden an einer Hochschule"
      },
      {
        "id": "bildung/kindertageseinrichtung/betreuungsplatz",
        "label": "Bildung – Kindertageseinrichtung - Betreuungsplatz",
        "definition": "Zur Verfügung stehende Betreuungsplätze in Kindertagesstätten"
      },
      {
        "id": "bildung/kindertageseinrichtung/standort",
        "label": "Bildung – Kindertageseinrichtung - Standort",
        "definition": "Standorte von Einrichtungen, in denen Kinder ganztägig betreut werden"
      },
      {
        "id": "bildung/musikschule/teilnehmerzahl",
        "label": "Bildung – Musikschule - Teilnehmerzahl",
        "definition": "Zahl der Personen, die an Unterricht oder Veranstaltungen der Musikschulen teilnehmen"
      },
      {
        "id": "bildung/musikschule/unterrichtsangebot",
        "label": "Bildung – Musikschule - Unterrichtsangebot",
        "definition": "Fächer, die an Musikschulen unterricht werden"
      },
      {
        "id": "bildung/schule/internetanbindung",
        "label": "Bildung – Schule - Internetanbindung",
        "definition": "Anbindung von Schulen ins Internet"
      },
      {
        "id": "bildung/schule/schuelerzahl",
        "label": "Bildung – Schule - Schülerzahl",
        "definition": "Anzahl der Schülerinnen und Schüler"
      },
      {
        "id": "bildung/schule/schulangebot",
        "label": "Bildung – Schule - Schulangebot",
        "definition": "Verzeichnisse der zur Verfügung stehenden Schulen bzw. deren Angebote"
      },
      {
        "id": "bildung/schule/schuleingangsuntersuchung",
        "label": "Bildung – Schule - Schuleingangsuntersuchung",
        "definition": "Gesetzlich vorgeschriebene Schulneulingsuntersuchung auf Einladung des Gesundheitsamtes vor der Aufnahme in die erste Jahrgangsstufe der Grundschule"
      },
      {
        "id": "bildung/schule/schulentwicklungsplan",
        "label": "Bildung – Schule - Schulentwicklungsplan",
        "definition": "Planungs- und Steuerungsinstrument für die Umsetzung schulischer Entwicklungsvorhaben"
      },
      {
        "id": "bildung/schule/standort",
        "label": "Bildung – Schule - Standort",
        "definition": "Standorte, an denen sich Schulen befinden"
      },
      {
        "id": "bildung/schule/wunschschule",
        "label": "Bildung – Schule - Wunschschule",
        "definition": "Angaben zur Wahl der Erstwunsch-Schule"
      },
      {
        "id": "bildung/volkshochschule/teilnehmerzahl",
        "label": "Bildung – Volkshochschule - Teilnehmerzahl",
        "definition": "Anzahl der am Angebot der Erwachsenenbildungsinstitute teilnehmenden Personen"
      },
      {
        "id": "bildung/volkshochschule/veranstaltung",
        "label": "Bildung – Volkshochschule - Veranstaltung",
        "definition": "Events, die an Erwachsenenbildungsinstituten stattfinden"
      },
      {
        "id": "buergerservice",
        "label": "Bürgerservice",
        "definition": "Zentrale Anlaufstelle, die Bürgerinnen und Bürgern Informationen und die Erledigung ihrer Anliegen aus erster Hand anbietet"
      },
      {
        "id": "buergerservice/anliegenmanagement",
        "label": "Bürgerservice – Anliegenmanagement",
        "definition": "Systeme, mit denen Anliegen, Beschwerden, Hinweise und Wünsche von Nutzerinnen und Nutzern öffentlicher Dienste eingereicht werden"
      },
      {
        "id": "buergerservice/dienstleistung",
        "label": "Bürgerservice – Dienstleistung",
        "definition": "Serviceangebote der Bürgerservicestellen"
      },
      {
        "id": "buergerservice/hundekottuete",
        "label": "Bürgerservice – Hundekottüte",
        "definition": "Standorte von Hundekotbeutelstationen"
      },
      {
        "id": "buergerservice/telefonverzeichnis",
        "label": "Bürgerservice – Telefonverzeichnis",
        "definition": "Telefonnummern von Mitarbeiterinnen und Mitarbeitern der Verwaltung"
      },
      {
        "id": "buergerservice/termin",
        "label": "Bürgerservice – Termin",
        "definition": "Termine und Öffnungszeiten von Einrichtungen der Kommunalverwaltung"
      },
      {
        "id": "buergerservice/wartezeit",
        "label": "Bürgerservice – Wartezeit",
        "definition": "Wartezeiten in Einrichtungen der Kommunalverwaltung"
      },
      {
        "id": "digitalisierung",
        "label": "Digitalisierung",
        "definition": "Digitale Transformation und Durchdringung aller Bereiche von Wirtschaft, Staat, Gesellschaft und Alltag"
      },
      {
        "id": "digitalisierung/openData/planung",
        "label": "Digitalisierung – Open Data - Planung",
        "definition": "Angaben zur Durchführung von Initiativen für offene Verwaltungsdaten"
      },
      {
        "id": "digitalisierung/openData/zugriffszahl",
        "label": "Digitalisierung – Open Data - Zugriffszahl",
        "definition": "Zahl der Aufrufe von offenen Verwaltungsdaten"
      },
      {
        "id": "digitalisierung/website",
        "label": "Digitalisierung – Website",
        "definition": "Zugriffstatistiken der kommunalen Websites"
      },
      {
        "id": "digitalisierung/wlanUndMobilfunk",
        "label": "Digitalisierung – WLAN und Mobilfunk",
        "definition": "Standorte von WLAN-Hotspots, Freifunkrouter und Mobilfunkstandorte"
      },
      {
        "id": "energie",
        "label": "Energie",
        "definition": "Fähigkeit, mechanische Arbeit zu verrichten, Wärme abzugeben oder Licht auszustrahlen"
      },
      {
        "id": "energie/energiebericht",
        "label": "Energie – Energiebericht",
        "definition": "Darstellungen im Bereich Energiemanagement und der Erfolge von durchgeführten Maßnahmen"
      },
      {
        "id": "energie/solar",
        "label": "Energie – Solar",
        "definition": "Solarenergiekataster bzw. Angaben zur erzeugten Solarenergie"
      },
      {
        "id": "energie/stromversorgung",
        "label": "Energie – Stromversorgung",
        "definition": "Kennzahlen zur Stromversorgung in einer Kommune"
      },
      {
        "id": "energie/waermeversorgung",
        "label": "Energie – Wärmeversorgung",
        "definition": "Kennzahlen zur Wärmeversorgung in einer Kommune"
      },
      {
        "id": "energie/wasserversorgung",
        "label": "Energie – Wasserversorgung",
        "definition": "Kennzahlen zur Wasserversorgung in einer Kommune"
      },
      {
        "id": "energie/windenergie",
        "label": "Energie – Windenergie",
        "definition": "Kennzahlen zur Versorgung mit Windenergie in einer Kommune"
      },
      {
        "id": "finanzen",
        "label": "Finanzen",
        "definition": "Finanzielle Gebahrung einer Kommune"
      },
      {
        "id": "finanzen/haushalt/ausserplanmaessigeAufwendungen",
        "label": "Finanzen – Haushalt - Außerplanmäßige Aufwendung",
        "definition": "Aufwendungen oder Auszahlungen, für die im Haushaltsplan keine Ermächtigungen veranschlagt und keine aus den Vorjahren übertragenen Ermächtigungen verfügbar sind"
      },
      {
        "id": "finanzen/haushalt/controlling",
        "label": "Finanzen – Haushalt - Controlling",
        "definition": "Überwachung des kommunalen Haushalts"
      },
      {
        "id": "finanzen/haushalt/jahresabschluss",
        "label": "Finanzen – Haushalt - Jahresabschluss",
        "definition": "Haushaltsrechnungen von Kommunen"
      },
      {
        "id": "finanzen/haushalt/plan",
        "label": "Finanzen – Haushalt - Plan",
        "definition": "Kommunale Haushaltspläne"
      },
      {
        "id": "finanzen/haushalt/produktplan",
        "label": "Finanzen – Haushalt - Produktplan",
        "definition": "Von einer öffentlichen Verwaltung erstellter, verwaltungsspezifischer Gliederungsplan, der die Produktstruktur im Haushaltsplan festlegt"
      },
      {
        "id": "finanzen/haushalt/satzung",
        "label": "Finanzen – Haushalt - Satzung",
        "definition": "Rechtsgrundlage für den Vollzug des Haushaltsplans in der kommunalen Verwaltung, der von der Gemeindevertretung oder dem Kreistag in öffentlicher Sitzung beschlossen wird"
      },
      {
        "id": "finanzen/haushalt/sponsoring",
        "label": "Finanzen – Haushalt - Sponsoring",
        "definition": "Unterstützungen seitens der Kommunen durch finanzielle Mittel bzw. Sach- oder Dienstleistungen"
      },
      {
        "id": "finanzen/haushalt/zuwendungUndFoerderung",
        "label": "Finanzen – Haushalt - Zuwendung und Förderung",
        "definition": "Finanzielle Zuwendungen aus dem kommunalen Budget"
      },
      {
        "id": "finanzen/steuernUndAbgaben",
        "label": "Finanzen – Steuern und Abgaben",
        "definition": "Aufkommen an Steuern, Beiträgen und Gebühren"
      },
      {
        "id": "floraUndFauna",
        "label": "Flora und Fauna",
        "definition": "Pflanzen- und Tierwelt"
      },
      {
        "id": "floraUndFauna/baumbestand/baumfaellung",
        "label": "Flora und Fauna – Baumbestand - Baumfällung",
        "definition": "Umschneiden von Bäumen"
      },
      {
        "id": "floraUndFauna/baumbestand/baumkataster",
        "label": "Flora und Fauna – Baumbestand - Baumkataster",
        "definition": "Verzeichnis, in dem Bäume inklusive Standort und weiteren Informationen verwaltet werden"
      },
      {
        "id": "floraUndFauna/flaeche/ausgleichsflaeche",
        "label": "Flora und Fauna – Fläche - Ausgleichsfläche",
        "definition": "Flächen für den Naturschutz, die bei Eingriffen in Natur und Landschaft, wie z. B. größere Bauprojekte, dafür sorgen, dass ein gewisser Ausgleich für negative ökologische Folgen geschaffen wird"
      },
      {
        "id": "floraUndFauna/flaeche/biotopflaeche",
        "label": "Flora und Fauna – Fläche - Biotopfläche",
        "definition": "Verzeichnis der Biotope in den Kommunen"
      },
      {
        "id": "floraUndFauna/flaeche/gruenflaecheUndGruenflaechenkataster",
        "label": "Flora und Fauna – Fläche - Grünfläche und Grünflächenkataster",
        "definition": "Verzeichnis der kommunalen Grünflächen meist mit Koppelung an ein Geoinformationssystem mit Angaben wie Fläche, Standort, Pflanzenbestand und Pflegemaßnahmen"
      },
      {
        "id": "floraUndFauna/flaeche/hundewiese",
        "label": "Flora und Fauna – Fläche - Hundewiese",
        "definition": "Standorte der kommunalen Hundeauslaufgebiete"
      },
      {
        "id": "floraUndFauna/flaeche/jagdbezirk",
        "label": "Flora und Fauna – Fläche - Jagdbezirk",
        "definition": "Kommunale Gebiete, in denen die Jagd ausgeübt wird"
      },
      {
        "id": "floraUndFauna/flaeche/naturschutzgebiet",
        "label": "Flora und Fauna – Fläche - Naturschutzgebiet",
        "definition": "Kommunale Gebiete, die unter Naturschutz stehen"
      },
      {
        "id": "floraUndFauna/flaeche/waldflaeche",
        "label": "Flora und Fauna – Fläche - Waldfläche",
        "definition": "Bewaldete kommunale Gebiete"
      },
      {
        "id": "floraUndFauna/gewaesser/pegelstand",
        "label": "Flora und Fauna – Gewässer - Pegelstand",
        "definition": "Wasserstände kommunaler Gewässer"
      },
      {
        "id": "floraUndFauna/gewaesser/wasserflaeche",
        "label": "Flora und Fauna – Gewässer - Wasserfläche",
        "definition": "Kommunale Gewässer"
      },
      {
        "id": "floraUndFauna/urbanGardening",
        "label": "Flora und Fauna – Urban Gardening",
        "definition": "Kleinräumige, gärtnerisch genutzte städtische Flächen"
      },
      {
        "id": "freizeit",
        "label": "Freizeit",
        "definition": "kommunale Freizeitangebote"
      },
      {
        "id": "freizeit/badUndFreibad",
        "label": "Freizeit – Bad und Freibad",
        "definition": "Standorte und Kennzahlen der kommunalen Schwimmbäder"
      },
      {
        "id": "freizeit/ferienangebot",
        "label": "Freizeit – Ferienangebot",
        "definition": "Während der Schulferien angebotene Freizeitaktivitäten für Kinder und Jugendliche "
      },
      {
        "id": "freizeit/grillplatz",
        "label": "Freizeit – Grillplatz",
        "definition": "Standorte öffentlicher Grillstellen"
      },
      {
        "id": "freizeit/jugendeinrichtung",
        "label": "Freizeit – Jugendeinrichtung",
        "definition": "Standorte bzw. Angebote der Einrichtungen der kommunalen Jugendhilfe"
      },
      {
        "id": "freizeit/sitzgelegenheit",
        "label": "Freizeit – Sitzgelegenheit",
        "definition": "Sitzplätze im öffentlichen Raum"
      },
      {
        "id": "freizeit/spielplatzUndSpielstaette",
        "label": "Freizeit – Spielplatz und Spielstätte",
        "definition": "Standorte bzw. Kennzahlen der kommunalen Spielanlagen"
      },
      {
        "id": "freizeit/verein",
        "label": "Freizeit – Verein",
        "definition": "Informationen zu Vereinen in Kommunen"
      },
      {
        "id": "geschichte",
        "label": "Geschichte",
        "definition": "Daten zum politischen, kulturellen und gesellschaftlichen Werdegang, Entwicklungsprozess einer Kommune"
      },
      {
        "id": "geschichte/quelle/archivbestand",
        "label": "Geschichte – Quelle - Archivbestand",
        "definition": "Bestände kommunaler Archive"
      },
      {
        "id": "geschichte/quelle/entschaedigung",
        "label": "Geschichte – Quelle - Entschädigung",
        "definition": "Kommunale Entschädigungsakten"
      },
      {
        "id": "geschichte/quelle/historischeKarte",
        "label": "Geschichte – Quelle - Historische Karte",
        "definition": "Daten zu historischen Landkarten"
      },
      {
        "id": "geschichte/quelle/historischeLuftaufnahme",
        "label": "Geschichte – Quelle - Historische Luftaufnahme",
        "definition": "Daten zu historischen Fotoaufnahmen der Kommunen aus der Luft"
      },
      {
        "id": "geschichte/quelle/personalverzeichnis",
        "label": "Geschichte – Quelle - Personalverzeichnis",
        "definition": "Kontaktliste kommunaler Mitarbeiterinnen und Mitarbeiter"
      },
      {
        "id": "geschichte/standortMitGeschichte",
        "label": "Geschichte – Standort mit Geschichte",
        "definition": "Orte mit geschichtlicher Relevanz"
      },
      {
        "id": "gesundheit",
        "label": "Gesundheit",
        "definition": "Daten zu kommunalen Gesundheitsdienstleistungen und -einrichtungen"
      },
      {
        "id": "gesundheit/apotheke",
        "label": "Gesundheit – Apotheke",
        "definition": "Standorte und weitere Angaben zu Apotheken"
      },
      {
        "id": "gesundheit/arzt",
        "label": "Gesundheit – Arzt",
        "definition": "Daten zu den Ärztinnen und Ärzten"
      },
      {
        "id": "gesundheit/gesundheitsberichterstattung",
        "label": "Gesundheit – Gesundheitsberichterstattung",
        "definition": "Kommunale Gesundheitsberichte"
      },
      {
        "id": "gesundheit/hebamme",
        "label": "Gesundheit – Hebamme",
        "definition": "Listen aller im Kommunalgebiet tätigen Hebammen"
      },
      {
        "id": "gesundheit/infektion",
        "label": "Gesundheit – Infektion",
        "definition": "Infektionsgeschehen in den Kommunen"
      },
      {
        "id": "gesundheit/krankenhaus",
        "label": "Gesundheit – Krankenhaus",
        "definition": "Standorte und Kennzahlen zu Krankenhäusern in einer Kommune"
      },
      {
        "id": "gesundheit/oeffentlicheToilette",
        "label": "Gesundheit – Öffentliche Toilette",
        "definition": "Informationen zu Standort und Austattung der öffentlichen Bedürfnisanstalten in einer Kommune"
      },
      {
        "id": "gesundheit/rettungsdienst/defibrillator",
        "label": "Gesundheit – Rettungsdienst - Defibrillator",
        "definition": "Standorte kommunaler Defibrillatoren"
      },
      {
        "id": "gesundheit/rettungsdienst/rettungsdiensteinsatz",
        "label": "Gesundheit – Rettungsdienst - Rettungsdiensteinsatz",
        "definition": "Kennzahlen zu Einsätzen durch die kommunalen Rettungsdienste"
      },
      {
        "id": "justiz",
        "label": "Justiz",
        "definition": "Für die Ausübung der Justiz verantwortliche Behörden und Einrichtungen"
      },
      {
        "id": "justiz/gesetzestext",
        "label": "Justiz – Gesetzestext",
        "definition": "Wortlaut eines Gesetzes"
      },
      {
        "id": "justiz/justizeinrichtung",
        "label": "Justiz – Justizeinrichtung",
        "definition": "Angaben über kommunale Justizstandorte"
      },
      {
        "id": "klimaschutzUndUmweltschutz",
        "label": "Klimaschutz und Umweltschutz",
        "definition": "Daten zu Witterung und Wettererscheinungen bzw.  zum Schutz der natürlichen Umwelt"
      },
      {
        "id": "klimaschutzUndUmweltschutz/berichtUndAnalyse/klimabilanz",
        "label": "Klimaschutz und Umweltschutz – Bericht und Analyse - Klimabilanz",
        "definition": "Kennzahlen zur Klimabilanz der Kommunen"
      },
      {
        "id": "klimaschutzUndUmweltschutz/berichtUndAnalyse/luftUndEmission",
        "label": "Klimaschutz und Umweltschutz – Bericht und Analyse - Luft und Emission",
        "definition": "Kennzahlen zu Luft- und Emissionswerten"
      },
      {
        "id": "klimaschutzUndUmweltschutz/berichtUndAnalyse/verkehrsmessung",
        "label": "Klimaschutz und Umweltschutz – Bericht und Analyse - Verkehrsmessung",
        "definition": "Kennzahlen zum Verkehrsaufkommen in einer Kommune"
      },
      {
        "id": "klimaschutzUndUmweltschutz/berichtUndAnalyse/wasser",
        "label": "Klimaschutz und Umweltschutz – Bericht und Analyse - Wasser",
        "definition": "Kennzahlen zu Wasser in einer Kommune"
      },
      {
        "id": "klimaschutzUndUmweltschutz/radioaktivitaetsmessung",
        "label": "Klimaschutz und Umweltschutz – Radioaktivitätsmessung",
        "definition": "Kennzahlen zu Radioaktivität in einer Kommune"
      },
      {
        "id": "klimaschutzUndUmweltschutz/umweltzone",
        "label": "Klimaschutz und Umweltschutz – Umweltzone",
        "definition": "Daten zu den in einer Kommune eingerichteten Gebieten, in denen nur Kfz mit Feinstaubplakette fahren dürfen"
      },
      {
        "id": "kultur",
        "label": "Kultur",
        "definition": "Daten zu Standort bzw. Angebot an geistigen, künstlerischen, gestaltenden Leistungen einer Kommune wie etwa Kunstwerke, Bauwerke (Museen, Theater, Denkmäler, Kirchen, Friedhöfe) usw."
      },
      {
        "id": "kultur/denkmal",
        "label": "Kultur – Denkmal",
        "definition": "Standorte und weitere Angaben zu Denkmälerm bzw. Erinnerungsorten in Kommunen"
      },
      {
        "id": "kultur/friedhof/grabstaette",
        "label": "Kultur – Friedhof - Grabstätte",
        "definition": "Standorte und Eigenschaften von Stellen, an denen Tote beerdigt sind"
      },
      {
        "id": "kultur/friedhof/standort",
        "label": "Kultur – Friedhof - Standort",
        "definition": "Standorte der Friedhöfe"
      },
      {
        "id": "kultur/kunstwerk",
        "label": "Kultur – Kunstwerk",
        "definition": "Daten zu Erzeugnissen künstlerischen Schaffens im öffentlichen Raum der Kommunen"
      },
      {
        "id": "kultur/lehrpfadUndWanderpfad",
        "label": "Kultur – Lehrpfad und Wanderpfad",
        "definition": "Daten zu Freizeitwegen inkl. gestalteten [Themen]wegen mit dem Ziel der Wissensvermittlung"
      },
      {
        "id": "kultur/museum/besucherzahl",
        "label": "Kultur – Museum - Besucherzahl",
        "definition": "Frequentierungszahlen in Museen"
      },
      {
        "id": "kultur/museum/standort",
        "label": "Kultur – Museum - Standort",
        "definition": "Standorte der Museen in Kommunen"
      },
      {
        "id": "kultur/religioeseEinrichtung",
        "label": "Kultur – religiöse Einrichtung",
        "definition": "Standorte bzw. Kennzahlen zu Sakralbauten, Gotteshäusern, Glaubenseinrichtungen"
      },
      {
        "id": "kultur/theater/besucherzahl",
        "label": "Kultur – Theater - Besucherzahl",
        "definition": "Anzahl der Besucherinnen und Besucher von Theatern"
      },
      {
        "id": "kultur/theater/programm",
        "label": "Kultur – Theater - Programm",
        "definition": "Informationen zu Theatervorstellungen"
      },
      {
        "id": "kultur/veranstaltung/angebot",
        "label": "Kultur – Veranstaltung - Angebot",
        "definition": "Informationen zu angebotenen Veranstaltungen"
      },
      {
        "id": "kultur/veranstaltung/besucherzahl",
        "label": "Kultur – Veranstaltung - Besucherzahl",
        "definition": "Anzahl der Besucherinnen und Besucher einer Veranstaltung"
      },
      {
        "id": "oeffentlichkeitsarbeit",
        "label": "Öffentlichkeitsarbeit",
        "definition": "öffentliche Kommunikation"
      },
      {
        "id": "oeffentlichkeitsarbeit/pressemitteilungUndVeroeffentlichung",
        "label": "Öffentlichkeitsarbeit – Pressemitteilung und Veröffentlichung",
        "definition": "Medienaussendungen und Pressemeldungen"
      },
      {
        "id": "oeffentlichkeitsarbeit/stadtmarketing",
        "label": "Öffentlichkeitsarbeit – Stadtmarketing",
        "definition": "Gesamtheit der Maßnahmen zur Imageförderung einer Stadt"
      },
      {
        "id": "politischePartizipation",
        "label": "Politische Partizipation",
        "definition": "Teilhabe und Beteiligung von Bürgerinnen und Bürgern an politischen Willensbildungs- und Entscheidungsprozessen"
      },
      {
        "id": "politischePartizipation/buergerbeteiligung/buergerentscheid",
        "label": "Politische Partizipation – Bürgerbeteiligung - Bürgerentscheid",
        "definition": "Entscheidung einer wichtigen Angelegenheit der Kommune durch die Bürgerinnen und Bürger"
      },
      {
        "id": "politischePartizipation/buergerbeteiligung/buergerhaushalt",
        "label": "Politische Partizipation – Bürgerbeteiligung - Bürgerhaushalt",
        "definition": "Direkte kommunale Bürgerbeteiligung, bei der die Bürgerinnen und Bürger über Teile der Haushaltsmittel mitbestimmen"
      },
      {
        "id": "politischePartizipation/buergerbeteiligung/entwicklungUndInformation",
        "label": "Politische Partizipation – Bürgerbeteiligung - Entwicklung und Information",
        "definition": "Information über und Weiterentwicklung der Bürgerbeteiligung"
      },
      {
        "id": "politischePartizipation/buergerbeteiligung/umfrage",
        "label": "Politische Partizipation – Bürgerbeteiligung - Umfrage",
        "definition": "Daten zu Befragungen von Bürgerinnen und Bürgern zu bestimmten Themen der Verwaltung"
      },
      {
        "id": "politischePartizipation/politischeVertretung/buergermeister",
        "label": "Politische Partizipation – Politische Vertretung - Bürgermeister",
        "definition": "Angaben zu den Bürgermeisterinnen und Bürgermeistern der Kommunen"
      },
      {
        "id": "politischePartizipation/politischeVertretung/gremium",
        "label": "Politische Partizipation – Politische Vertretung - Gremium",
        "definition": "Informationen zu den beschlussfassenden Ausschüssen der Kommunen"
      },
      {
        "id": "politischePartizipation/politischeVertretung/mandatstraeger",
        "label": "Politische Partizipation – Politische Vertretung - Mandatsträger",
        "definition": "Informationen zu Mandatsträgerinnen und Mandatsträgern der Kommunen"
      },
      {
        "id": "politischePartizipation/verband",
        "label": "Politische Partizipation – Verband",
        "definition": "Zusammenschluss mehrerer kleinerer Vereinigungen oder Einzelpersonen zur Durchsetzung gemeinsamer Interessen"
      },
      {
        "id": "politischePartizipation/wahl/beiratswahl",
        "label": "Politische Partizipation – Wahl - Beiratswahl",
        "definition": "Informationen über die Wahlen kommunaler Beiräte"
      },
      {
        "id": "politischePartizipation/wahl/bundestagswahl",
        "label": "Politische Partizipation – Wahl - Bundestagswahl",
        "definition": "Wahleinrichtungen bzw. Wahlergebnisse der Bundestagswahl"
      },
      {
        "id": "politischePartizipation/wahl/europawahl",
        "label": "Politische Partizipation – Wahl - Europawahl",
        "definition": "Wahleinrichtungen bzw. Wahlergebnisse der Europawahl"
      },
      {
        "id": "politischePartizipation/wahl/kandidatenliste",
        "label": "Politische Partizipation – Wahl - Kandidatenliste",
        "definition": "Wahlvorschläge der Kommunen"
      },
      {
        "id": "politischePartizipation/wahl/kommunalwahl",
        "label": "Politische Partizipation – Wahl - Kommunalwahl",
        "definition": "Wahleinrichtungen bzw. Wahlergebnisse von Kommunalwahlen"
      },
      {
        "id": "politischePartizipation/wahl/landtagswahl",
        "label": "Politische Partizipation – Wahl - Landtagswahl",
        "definition": "Wahleinrichtungen bzw. Wahlergebnisse der Landtagswahl"
      },
      {
        "id": "politischePartizipation/wahl/strassenverzeichnis",
        "label": "Politische Partizipation – Wahl - Straßenverzeichnis",
        "definition": "Für Wahlen erstelltes Verzeichnis der Straßen und Plätze einer Kommune nach Stimmbezirk, Wahlbezirk, Wahlkreis"
      },
      {
        "id": "politischePartizipation/wahl/verbundwahl",
        "label": "Politische Partizipation – Wahl - Verbundwahl",
        "definition": "Durch Zusammenlegung gleichzeitig stattfindende Wahlen"
      },
      {
        "id": "politischePartizipation/wahl/wahlkreisUndWahlbezirk",
        "label": "Politische Partizipation – Wahl - Wahlkreis und Wahlbezirk",
        "definition": "Daten zu Wahlkreisen und Wahlbezirken"
      },
      {
        "id": "politischePartizipation/wahl/wahllokal",
        "label": "Politische Partizipation – Wahl - Wahllokal",
        "definition": "Daten zu Orten der Wahlaustragung"
      },
      {
        "id": "raumplanung",
        "label": "Raumplanung",
        "definition": "Daten zu Raumordnung, Raumplanung und Raumentwicklung"
      },
      {
        "id": "raumplanung/bauleitplan",
        "label": "Raumplanung – Bauleitplan",
        "definition": "Daten zu städtebaulichen Entwicklungsplänen"
      },
      {
        "id": "raumplanung/bebauungsplan",
        "label": "Raumplanung – Bebauungsplan",
        "definition": "Kommunale Plänen, nach denen Flächen bebaut werden sollen"
      },
      {
        "id": "raumplanung/flaechennutzung",
        "label": "Raumplanung – Flächennutzung",
        "definition": "Nutzung größerer Flächen einer Kommune für bestimmte Zwecke"
      },
      {
        "id": "raumplanung/liegenschaft/grundstueckUndGebaeude",
        "label": "Raumplanung – Liegenschaft - Grundstück und Gebäude",
        "definition": "Daten zu kommunalen Liegenschaften"
      },
      {
        "id": "raumplanung/liegenschaft/liegenschaftskataster",
        "label": "Raumplanung – Liegenschaft - Liegenschaftskataster",
        "definition": "Daten zum Grundstücksverzeichnis"
      },
      {
        "id": "raumplanung/liegenschaft/satzung",
        "label": "Raumplanung – Liegenschaft - Satzung",
        "definition": "Satzungen im Bereich Liegenschaften"
      },
      {
        "id": "raumplanung/orthofoto",
        "label": "Raumplanung – Orthofoto",
        "definition": "Verzerrungsfreie, maßstabsgetreue aus Luft- oder Satellitenbildern abgeleitete Abbildungen der Erdoberfläche"
      },
      {
        "id": "raumplanung/raumgliederung/adresse",
        "label": "Raumplanung – Raumgliederung - Adresse",
        "definition": "Daten zu Anschriften"
      },
      {
        "id": "raumplanung/raumgliederung/block",
        "label": "Raumplanung – Raumgliederung - Block",
        "definition": "Beschreibung von Gebieten innerhalb eines Stadtteils, die als Blöcke bezeichnet werden"
      },
      {
        "id": "raumplanung/raumgliederung/hausnummer",
        "label": "Raumplanung – Raumgliederung - Hausnummer",
        "definition": "Daten zu den Nummern der einzelnen Häuser"
      },
      {
        "id": "raumplanung/raumgliederung/ortsteil",
        "label": "Raumplanung – Raumgliederung - Ortsteil",
        "definition": "Daten zur kommunalen Gliederung in Stadtteile"
      },
      {
        "id": "raumplanung/raumgliederung/postleitzahlengebiet",
        "label": "Raumplanung – Raumgliederung - Postleitzahlengebiet",
        "definition": "Postleitzahlen von Städten und Gemeinden"
      },
      {
        "id": "raumplanung/raumgliederung/stadtgebiet",
        "label": "Raumplanung – Raumgliederung - Stadtgebiet",
        "definition": "Informationen zu Stadtgebieten"
      },
      {
        "id": "raumplanung/raumgliederung/strasse",
        "label": "Raumplanung – Raumgliederung - Straße",
        "definition": "Informationen zu Straßen"
      },
      {
        "id": "raumplanung/sozialraum",
        "label": "Raumplanung – Sozialraum",
        "definition": "Daten zu Sozialraum als Stadtplanungs- und Verwaltungskategorie"
      },
      {
        "id": "raumplanung/stadtplan",
        "label": "Raumplanung – Stadtplan",
        "definition": "Kartographische Daten einer Stadt"
      },
      {
        "id": "sicherheit",
        "label": "Sicherheit",
        "definition": "Daten zu kommunalen Sicherheitsthemen"
      },
      {
        "id": "sicherheit/beleuchtung",
        "label": "Sicherheit – Beleuchtung",
        "definition": "Daten zur öffentlichen Beleuchtung"
      },
      {
        "id": "sicherheit/feuerwehr/feuerwehreinsatz",
        "label": "Sicherheit – Feuerwehr - Feuerwehreinsatz",
        "definition": "Daten zu Einsätzen der Feuerwehr in den Kommunen"
      },
      {
        "id": "sicherheit/feuerwehr/personal",
        "label": "Sicherheit – Feuerwehr - Personal",
        "definition": "Daten zu den im Feuerwehrdienst tätigen Einsatzkräften"
      },
      {
        "id": "sicherheit/feuerwehr/standort",
        "label": "Sicherheit – Feuerwehr - Standort",
        "definition": "Verzeichnis der Feuerwehrstandorte"
      },
      {
        "id": "sicherheit/kriminalitaetsstatistik",
        "label": "Sicherheit – Kriminalitätsstatistik",
        "definition": "Daten zur Kriminalität"
      },
      {
        "id": "sicherheit/ordnungsamt",
        "label": "Sicherheit – Ordnungsamt",
        "definition": "Informationen über die Tätigkeit der für die Abwehr von Gefahren für die öffentliche Sicherheit oder Ordnung verantwortliche Organisationseinheit der Kommunalverwaltung"
      },
      {
        "id": "sicherheit/polizei",
        "label": "Sicherheit – Polizei",
        "definition": "Standorte der Polizei"
      },
      {
        "id": "sicherheit/rettungshilfe/anlaufstelle",
        "label": "Sicherheit – Rettungshilfe - Anlaufstelle",
        "definition": "Kontaktstellen der Institutionen, Organisationen oder Personen, an die man sich im Notfall wenden kann, um Hilfe oder Unterstützung zu bekommen (z. B. bei Feuer, Lebensgefahr, medizinischer Notlage)"
      },
      {
        "id": "sicherheit/rettungshilfe/notfallnummer",
        "label": "Sicherheit – Rettungshilfe - Notfallnummer",
        "definition": "Öffentliche Orte, die mit Informationen zu Notfallnummern ausgestattet sind"
      },
      {
        "id": "sicherheit/rettungshilfe/notinsel",
        "label": "Sicherheit – Rettungshilfe - Notinsel",
        "definition": "Standorte von Anlaufpunkten, die Kindern in Not im Rahmen des Projekts 'Notinsel' als Zuflucht dienen"
      },
      {
        "id": "sicherheit/rettungshilfe/waldrettungspunkt",
        "label": "Sicherheit – Rettungshilfe - Waldrettungspunkt",
        "definition": "Waldstandorte für die Notfallalarmierung"
      },
      {
        "id": "sicherheit/zivilschutzUndKatastrophenschutz/kampfmittelfund",
        "label": "Sicherheit – Zivilschutz und Katastrophenschutz - Kampfmittelfund",
        "definition": "Daten zu Kampfmittelfunden und deren Beseitigung"
      },
      {
        "id": "sicherheit/zivilschutzUndKatastrophenschutz/sirene",
        "label": "Sicherheit – Zivilschutz und Katastrophenschutz - Sirene",
        "definition": "Standorte der und Informationen zu Zivilschutzsirenen"
      },
      {
        "id": "sonstiges",
        "label": "Sonstiges",
        "definition": "Unter Sonstiges werden Daten eingeordnet, die nicht in die übrigen Kategorien passen. Im Zuge von Weiterentwicklungen könnten aus diesen Datensätzen neue Kategorien gebildet werden."
      },
      {
        "id": "sonstiges/sonstiges",
        "label": "Sonstiges",
        "definition": "Unter Sonstiges werden Daten eingeordnet, die nicht in die übrigen Kategorien passen. Im Zuge von Weiterentwicklungen könnten aus diesen Datensätzen neue Kategorien gebildet werden."
      },
      {
        "id": "sozialeHilfe",
        "label": "Soziale Hilfe",
        "definition": "Daten zu Hilfen von öffentlichen Stellen in sozialen Notlagen"
      },
      {
        "id": "sozialeHilfe/angebotUndBeratungsstelle",
        "label": "Soziale Hilfe – Angebot und Beratungsstelle",
        "definition": "Verzeichnis des öffentlichen Angebotes sozialer Hilfen bzw. der Beratungsstellen"
      },
      {
        "id": "sozialeHilfe/behinderung/behindertenwohnheim",
        "label": "Soziale Hilfe – Behinderung - Behindertenwohnheim",
        "definition": "Einrichtungen für Menschen mit Behinderung"
      },
      {
        "id": "sozialeHilfe/behinderung/menschenMitBehinderung",
        "label": "Soziale Hilfe – Behinderung - Menschen mit Behinderung",
        "definition": "Informationen zu Menschen mit Behinderung"
      },
      {
        "id": "sozialeHilfe/bericht",
        "label": "Soziale Hilfe – Bericht",
        "definition": "Berichte über soziale Hilfestellungen"
      },
      {
        "id": "sozialeHilfe/finanzielleUnterstuetzung/foerderung",
        "label": "Soziale Hilfe – Finanzielle Unterstützung - Förderung",
        "definition": "Finanzielle Unterstützungen im Rahmen der sozialen Hilfe"
      },
      {
        "id": "sozialeHilfe/finanzielleUnterstuetzung/grundsicherung",
        "label": "Soziale Hilfe – Finanzielle Unterstützung - Grundsicherung",
        "definition": "Informationen zum Leistungsbezug der Grundsicherung"
      },
      {
        "id": "sozialeHilfe/finanzielleUnterstuetzung/wohngeld",
        "label": "Soziale Hilfe – Finanzielle Unterstützung - Wohngeld",
        "definition": "Statistische Informationen zu Empfängerinnen und Empfängern von Wohngeld"
      },
      {
        "id": "sozialeHilfe/flucht/asylbewerber",
        "label": "Soziale Hilfe – Flucht - Asylbewerber",
        "definition": "Statistische Informationen zu Leistungsbeziehenden nach dem Asylbewerberleistungsgesetz"
      },
      {
        "id": "sozialeHilfe/flucht/fluechtlingsunterbringung",
        "label": "Soziale Hilfe – Flucht - Flüchtlingsunterbringung",
        "definition": "Entwicklung der Unterbringung von Flüchtlingen"
      },
      {
        "id": "sozialeHilfe/flucht/fluechtlingszahl",
        "label": "Soziale Hilfe – Flucht - Flüchtlingszahl",
        "definition": "Zahl der Flüchtlinge"
      },
      {
        "id": "sozialeHilfe/flucht/integration",
        "label": "Soziale Hilfe – Flucht - Integration",
        "definition": "Informationen zu den Angeboten der Flüchtlingshilfe"
      },
      {
        "id": "sozialeHilfe/gefoerderterWohnungsbau",
        "label": "Soziale Hilfe – Geförderter Wohnungsbau",
        "definition": "Kennzahlen zu öffentlich geförderten Wohnungen"
      },
      {
        "id": "sozialeHilfe/pflege",
        "label": "Soziale Hilfe – Pflege",
        "definition": "Informationen zu Pflegepersonal und Pflegeeinrichtungen"
      },
      {
        "id": "staedtischesPersonal",
        "label": "Städtisches Personal",
        "definition": "Informationen zu städtischem Personal, wie etwa zu Stellenangeboten und -plänen sowie Bewerber- und Besoldungsstatistiken"
      },
      {
        "id": "staedtischesPersonal/stellenausschreibung",
        "label": "Städtisches Personal – Stellenausschreibung",
        "definition": "Städtische Stellenangebote"
      },
      {
        "id": "staedtischesPersonal/stellenplan",
        "label": "Städtisches Personal – Stellenplan",
        "definition": "Plan der Stellen im städtischen Dienst"
      },
      {
        "id": "tourismus",
        "label": "Tourismus",
        "definition": "Informationen zum Städtetourismus"
      },
      {
        "id": "tourismus/gaestezahl",
        "label": "Tourismus – Gästezahl",
        "definition": "Zahl der Gäste und Übernachtungen"
      },
      {
        "id": "tourismus/sehenswuerdigkeit",
        "label": "Tourismus – Sehenswürdigkeit",
        "definition": "Touristenattraktionen"
      },
      {
        "id": "tourismus/stadtfuehrung",
        "label": "Tourismus – Stadtführung",
        "definition": "Informationen zu Stadtrundgängen und touristischen Führungen"
      },
      {
        "id": "tourismus/unterkunft/campingplatz",
        "label": "Tourismus – Unterkunft - Campingplatz",
        "definition": "Verzeichnis der Campingplätze"
      },
      {
        "id": "tourismus/unterkunft/herberge",
        "label": "Tourismus – Unterkunft - Herberge",
        "definition": "Informationen zu Beherbergungen"
      },
      {
        "id": "tourismus/unterkunft/hotel",
        "label": "Tourismus – Unterkunft - Hotel",
        "definition": "Standorte und Kontaktdetails der Hotelbetriebe"
      },
      {
        "id": "tourismus/unterkunft/privatunterkunft",
        "label": "Tourismus – Unterkunft - Privatunterkunft",
        "definition": "Privatunterkünfte und Übernachtungsmöglichkeiten"
      },
      {
        "id": "verkehr",
        "label": "Verkehr",
        "definition": "Angaben zu Fortbewegungsarten und Verkehrsinfrastruktur"
      },
      {
        "id": "verkehr/ampelanlage",
        "label": "Verkehr – Ampelanlage",
        "definition": "Standorte der Ampelanlagen"
      },
      {
        "id": "verkehr/flugverkehr/flugbewegung",
        "label": "Verkehr – Flugverkehr - Flugbewegung",
        "definition": "Flugbewegungen und Fluggastaufkommen"
      },
      {
        "id": "verkehr/flugverkehr/flughafen",
        "label": "Verkehr – Flugverkehr - Flughafen",
        "definition": "Standorte und weitere Informationen zu Flughäfen"
      },
      {
        "id": "verkehr/fussverkehr/fussgaengerzone",
        "label": "Verkehr – Fußverkehr - Fußgängerzone",
        "definition": "Verkehrsflächen, auf denen Fußgängerinnen und Fußgänger Vorrang oder ausschließliches Nutzungsrecht gegenüber anderen Verkehrsteilnehmerinnen und Verkehrsteilnehmern haben"
      },
      {
        "id": "verkehr/fussverkehr/gehweg",
        "label": "Verkehr – Fußverkehr - Gehweg",
        "definition": "Bürgersteige"
      },
      {
        "id": "verkehr/fussverkehr/laufstreckeUndWanderstrecke",
        "label": "Verkehr – Fußverkehr - Laufstrecke und Wanderstrecke",
        "definition": "Strecken zum Laufen und Wandern in Kommunen"
      },
      {
        "id": "verkehr/kfz/Taxistand",
        "label": "Verkehr – KFZ - Taxistand",
        "definition": "Standorte der Taxihalteplätze"
      },
      {
        "id": "verkehr/kfz/autobahn",
        "label": "Verkehr – KFZ - Autobahn",
        "definition": "Informationen zum Autobahn-Straßennetz"
      },
      {
        "id": "verkehr/kfz/bussgeld",
        "label": "Verkehr – KFZ - Bußgeld",
        "definition": "Bußgelddaten"
      },
      {
        "id": "verkehr/kfz/carsharing",
        "label": "Verkehr – KFZ - Carsharing",
        "definition": "Standorte und Fahrzeuge des Carsharing-Angebots"
      },
      {
        "id": "verkehr/kfz/elektrotankstelle",
        "label": "Verkehr – KFZ - Elektrotankstelle",
        "definition": "E-Tankstellen zur Aufladung von Elektrofahrzeugen"
      },
      {
        "id": "verkehr/kfz/fahrzeugzulassung",
        "label": "Verkehr – KFZ - Fahrzeugzulassung",
        "definition": "Statistiken zur Straßenverkehrszulassung von Fahrzeugen"
      },
      {
        "id": "verkehr/kfz/messung",
        "label": "Verkehr – KFZ - Messung",
        "definition": "KFZ-Zählung und Geschwindigkeitsüberwachung"
      },
      {
        "id": "verkehr/kfz/parkplatz",
        "label": "Verkehr – KFZ - Parkplatz",
        "definition": "Parkberechtigungen, Parkhäuser, Parkflächen"
      },
      {
        "id": "verkehr/kfz/tankstelle",
        "label": "Verkehr – KFZ - Tankstelle",
        "definition": "Daten zu Tankstellen"
      },
      {
        "id": "verkehr/oepnv/aufzugUndRolltreppe",
        "label": "Verkehr – ÖPNV - Aufzug und Rolltreppe",
        "definition": "Rolltreppen und Aufzüge im öffentlichen Personennahverkehr"
      },
      {
        "id": "verkehr/oepnv/fahrgastzahl",
        "label": "Verkehr – ÖPNV - Fahrgastzahl",
        "definition": "Passagieraufkommen im kommunalen öffentlichen Personennahverkehr"
      },
      {
        "id": "verkehr/oepnv/liniennetzSollfahrdatenEchtzeitdaten",
        "label": "Verkehr – ÖPNV - Liniennetz Sollfahrdaten Echtzeitdaten",
        "definition": "Netz der kommunalen Verkehrslinien bzw. Ist- und Sollfahrdaten"
      },
      {
        "id": "verkehr/oepnv/vertriebsstelle",
        "label": "Verkehr – ÖPNV - Vertriebsstelle",
        "definition": "Standorte der Verkaufsstellen, Servicestellen und Fahrkartenautomaten im ÖPNV"
      },
      {
        "id": "verkehr/radverkehr/abstellplatz",
        "label": "Verkehr – Radverkehr - Abstellplatz",
        "definition": "Standorte der Fahrradstellplätze"
      },
      {
        "id": "verkehr/radverkehr/ladestation",
        "label": "Verkehr – Radverkehr - Ladestation",
        "definition": "E-Tankstellen zur Aufladung von Elektrofahrrädern"
      },
      {
        "id": "verkehr/radverkehr/messung",
        "label": "Verkehr – Radverkehr - Messung",
        "definition": "Standorte und Messergebnisse der Radzählstellen"
      },
      {
        "id": "verkehr/radverkehr/radwegUndRadroute",
        "label": "Verkehr – Radverkehr - Radweg und Radroute",
        "definition": "Informationen zu Radwegen und Radrouten"
      },
      {
        "id": "verkehr/radverkehr/verleih",
        "label": "Verkehr – Radverkehr - Verleih",
        "definition": "Standorte der Fahrradmietsysteme"
      },
      {
        "id": "verkehr/schiffsverkehrUndFaehrverkehr/anlegestelle",
        "label": "Verkehr – Schiffsverkehr und Fährverkehr - Anlegestelle",
        "definition": "Standorte der Schiffsanlegestellen und deren Belegung"
      },
      {
        "id": "verkehr/schiffsverkehrUndFaehrverkehr/fracht",
        "label": "Verkehr – Schiffsverkehr und Fährverkehr - Fracht",
        "definition": "Güterumschlag"
      },
      {
        "id": "verkehr/schiffsverkehrUndFaehrverkehr/passagier",
        "label": "Verkehr – Schiffsverkehr und Fährverkehr - Passagier",
        "definition": "Fahrgäste"
      },
      {
        "id": "verkehr/sondernutzung",
        "label": "Verkehr – Sondernutzung",
        "definition": "Anträge auf Ausnahmegenehmigungen und Erlaubnisse im Straßenverkehr"
      },
      {
        "id": "verkehr/unfall",
        "label": "Verkehr – Unfall",
        "definition": "Verkehrsunfälle, Verkehrsunfallentwicklung"
      },
      {
        "id": "wetter",
        "label": "Wetter",
        "definition": "Wetterdaten"
      },
      {
        "id": "wetter/hitze",
        "label": "Wetter – Hitze",
        "definition": "Hitzebelastung und Hitzeinseln im Stadtgebiet"
      },
      {
        "id": "wetter/messung",
        "label": "Wetter – Messung",
        "definition": "Wettermessdaten"
      },
      {
        "id": "wirtschaft",
        "label": "Wirtschaft",
        "definition": "Wirtschaftsdaten"
      },
      {
        "id": "wirtschaft/arbeitslosigkeit",
        "label": "Wirtschaft – Arbeitslosigkeit",
        "definition": "Statistische Daten zu Arbeitslosigkeit"
      },
      {
        "id": "wirtschaft/berufspendler",
        "label": "Wirtschaft – Berufspendler",
        "definition": "Infomationen zu Pendlerinnen und Pendlern, die regelmäßig zwischen Wohnort und Arbeitsplatz pendeln"
      },
      {
        "id": "wirtschaft/beschaeftigung",
        "label": "Wirtschaft – Beschäftigung",
        "definition": "Statistische Daten zu Beschäftigung"
      },
      {
        "id": "wirtschaft/beteiligungAnOeffentlicherWirtschaft/ausschreibungUndVergabe",
        "label": "Wirtschaft – Beteiligung an Öffentlicher Wirtschaft - Ausschreibung und Vergabe",
        "definition": "Vergaben und Ausschreibungen"
      },
      {
        "id": "wirtschaft/beteiligungAnOeffentlicherWirtschaft/beteiligung",
        "label": "Wirtschaft – Beteiligung an Öffentlicher Wirtschaft - Beteiligung",
        "definition": "Anteile der Kommunen an Unternehmen der Daseinsvorsorge"
      },
      {
        "id": "wirtschaft/bueroflaecheIndustrieflaecheGewerbeflaeche",
        "label": "Wirtschaft – Bürofläche Industriefläche Gewerbefläche",
        "definition": "Gewerblich genutzte Flächen"
      },
      {
        "id": "wirtschaft/coworking",
        "label": "Wirtschaft – Coworking",
        "definition": "Gemeinsam genutzte bzw. geteilte Büroräumlichkeiten"
      },
      {
        "id": "wirtschaft/dienstleistung/einzelhandel",
        "label": "Wirtschaft – Dienstleistung - Einzelhandel",
        "definition": "Einzelhandelsgeschäft"
      },
      {
        "id": "wirtschaft/dienstleistung/handwerk",
        "label": "Wirtschaft – Dienstleistung - Handwerk",
        "definition": "Gewerbliche Tätigkeiten, die dem Handwerk zugeordnet werden (nicht industriell)"
      },
      {
        "id": "wirtschaft/dienstleistung/postfiliale",
        "label": "Wirtschaft – Dienstleistung - Postfiliale",
        "definition": "Filialen der Postdienste"
      },
      {
        "id": "wirtschaft/dienstleistung/weihnachtsmarkt",
        "label": "Wirtschaft – Dienstleistung - Weihnachtsmarkt",
        "definition": "Weihnachtsmärkte"
      },
      {
        "id": "wirtschaft/dienstleistung/wochenmarkt",
        "label": "Wirtschaft – Dienstleistung - Wochenmarkt",
        "definition": "Regelmäßig stattfindende Märkte, besonders für Gemüse, Obst, Fleisch, Blumen"
      },
      {
        "id": "wirtschaft/gewerbeanmeldung",
        "label": "Wirtschaft – Gewerbeanmeldung",
        "definition": "Anmeldung der Ausübung eines Gewerbes bei der Behörde"
      },
      {
        "id": "wirtschaft/insolvenz",
        "label": "Wirtschaft – Insolvenz",
        "definition": "Unternehmensinsolvenzen"
      },
      {
        "id": "wirtschaft/wirtschaftsfoerderung",
        "label": "Wirtschaft – Wirtschaftsförderung",
        "definition": "Förderung der Wirtschaft durch Kommunen durch finanzielle oder andere Zuwendungen"
      },
      {
        "id": "wirtschaft/wirtschaftsstandort",
        "label": "Wirtschaft – Wirtschaftsstandort",
        "definition": "Wirtschaftsrahmenbedingungen in einem bestimmten Gebiet"
      }
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
