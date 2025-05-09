# Changelog

## Development

## [1.0.0-dev](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/1.0.0-dev)

_(2025-05-20)_

- Implement [berlin.de styleguide](https://styleguide.berlin.de/).

## [0.3.14](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.14)

_(2025-03-31)_

- Extend the list of HVDs beyond top-concepts.

## [0.3.13](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.13)

_(2024-12-17)_

- Add [publiccode.yml](publiccode.yml) for OpenCode.
- Change BerlinOnline company name more (drop the "Stadtportal").
- Adjust README.

## [0.3.12](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.12)

_(2024-08-28)_

- Change BerlinOnline company name (drop the "& Co. KG") everywhere.

## [0.3.11](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.11)

_(2024-08-05)_

- Update /about and /datenschutzerklaerung pages (responsible person & contact email address).

## [0.3.10](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.10)

_(2024-04-25)_

- Add functionality to mark organizations as external. This currently works with just an extra field `external` set to `true` on the organization. There is a helper function `org_is_external` (`berlin_org_is_external` in the template) to determine if an org is external, based on the extra.
- Add new metadata field `hvd_category` (to link to the category of high-value datasets as defined by the [EU commission implementing regulation 2023/138](https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj?uri=CELEX:32023R0138)).
- Add new metadata field `sample_record` (to link to the matching "Musterdatensatz", see https://www.dcat-ap.de/def/dcatde/2.0/implRules/#verwendung-des-musterdatenkatalogs-fur-kommunen).

## [0.3.9](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.9)

_(2024-03-22)_

- Use the new field `preview_image` (see [ckanext-berlin_dataset_schema](https://github.com/berlinonline/ckanext-berlin_dataset_schema)).
- Change Solr image reference in github CI ([test.yml](.github/workflows/test.yml)) to the new naming scheme according to https://github.com/ckan/ckan-solr.


## [0.3.8](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.8)

_(2023-07-14)_

- Remove some template code that got pasted accidentally into the breadcrumb.
- Don't show and link technical org in breadcrumb for non-admin users on dataset pages.
- Adjust tld-test for instance indicator ribbon ('.test' now shows 'LOCAL').

## [0.3.7](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.7)

_(2023-06-26)_

- Don't truncate author ('Quelle') names in facet list so quickly (40 instead of 20 characters).
- Add missing template (`package/base.html`).
- Update about/Impressum and privacy policy (_Senatskanzlei_ instead of _Senatsverwaltung für Inneres, Digitalisierung und Sport_).

## [0.3.6](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.6)

_(2023-05-19)_

- Append to `berlin.public_pages` config, rather than replace it.
- Define extension's version string in [VERSION](VERSION), make it available as `ckanext.berlintheme.__version__` and in [setup.py](setup.py).

## [0.3.5](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.5)

_(2023-05-08)_

- Fix problem where non-admin users would get an error when looking at the page for a dataset that belongs to a 'technical' organization (`simplesearch` etc.).
They are now shown a generic placeholder instead of the actual organization info.

## [0.3.4](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.4)

_(2023-04-16)_

- Configure `/about` (Impressum) and `/datenschutzerklaerung` to be publicly available using `berlin.public_pages` setting.
- Update `/about` and `/datenschutzerklaerung` for SenInnDS.
- Add spacing for `address`-elements.

## [0.3.3](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.3)

_(2023-04-14)_

- Remove error_document_template.html, we're just using the default template from
CKAN core for now.
- Remove reference to deprecated route in template.
- Fix and extend tests for figuring out which instance we're running on.

## [0.3.2](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.2)

_(2023-01-22)_

- Fix `Manifest.in`.

## [0.3.1](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.1)

_(2022-03-30)_

- Remove `classes_for_attribute()` helper, as it's no longer needed.

## [0.3.0](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.3.0)

_(2022-03-30)_

- Convert to Python 3.
- Switch routing from IRoutes (Pylons) to IBlueprint (Flask).
- Switch assets from Fanstatic to Webassets.
- Rewrite templates to work with CKAN Core 2.9 templates.
- Replace old PNG logos with inline SVG.
- Add unit tests and github CI.
- Reformat changelog, add dates and version links.
- Update README.
- This is the first version that requires Python 3 / CKAN >= 2.9.


## [0.2.1](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.2.1)

_(2020-06-19)_

- Add license (AGPL-3.0).
- Small updates to readme.
- This is the last version to work with Python 2 / CKAN versions < 2.9.

## [0.2.0](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.2.0)

_(2020-06-19)_

- Start a real changelog.
- Add privacy policy page ("Datenschutzerklärung")
- Various helpers added.
- Implement theming of required metadata.
- Implement theming of validation.

## [0.1.0](https://github.com/berlinonline/ckanext-berlintheme/releases/tag/0.1.0)

_(2018-05-19)_

- initial setup
- theming moved here from ckanext-berlin
