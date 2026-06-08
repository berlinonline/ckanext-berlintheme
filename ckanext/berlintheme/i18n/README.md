# Adding Translations

see https://docs.ckan.org/en/2.9/extensions/translating-extensions.html

But basically:

- Add `msgid` (English original) and `msgstr` (translated string) to `.po` file for desired language ([ckanext/berlintheme/i18n/de/LC_MESSAGES/ckanext-berlintheme.po](de/LC_MESSAGES/ckanext-berlintheme.po) in our case).
- In extension root, run:

```
$ python setup.py compile_catalog
```

- If you get `catalog ckanext/berlintheme/i18n/de/LC_MESSAGES/ckanext-berlintheme.po is marked as fuzzy, skipping`, you need to force the command:

```
$ python setup.py compile_catalog -f
```

- That updates the compiled `.mo` file.
