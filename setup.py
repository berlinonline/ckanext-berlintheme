from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-berlintheme',
	version=version,
	description="Berlin Open Data Portal CKAN extension (Theme/UI only)",
	long_description="""\
	Contains the Theme/UI definitions for the Berlin Open Data Portal.
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Knud M\xc3\xb6ller',
	author_email='knud.moeller@berlinonline.de',
	url='https://github.com/berlinonline/ckanext-berlintheme',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.berlintheme'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	         berlintheme=ckanext.berlintheme.plugin:BerlinTheme
	""",
)
