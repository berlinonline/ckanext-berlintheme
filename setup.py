from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='ckanext-berlintheme',
	version='0.3.5',
	description="Theming/UI extension for the Datenregister (CKAN instance for Berlin's Open Data portal)",
	long_description=long_description,

	url='https://github.com/berlinonline/ckanext-berlintheme',

  # author details
	author='Knud Möller',
	author_email='knud.moeller@berlinonline.de',
	
  license='AGPL',

  # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    'Development Status :: 4 - Beta',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
  ],

	keywords='''CKAN ITemplateHelpers IBlueprint theme ui templates''',

	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	namespace_packages=['ckanext'],
	
  install_requires=[],

	include_package_data=True,
	zip_safe=False,
	entry_points=\
	"""
    [ckan.plugins]
	  berlintheme=ckanext.berlintheme.plugin:BerlinTheme

    [babel.extractors]
    ckan = ckan.lib.extract:extract_ckan
	""",
)
