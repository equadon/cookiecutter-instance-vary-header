# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# CC Vary Header is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('cc_vary_header', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='cc-vary-header',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='cc-vary-header Invenio',
    license='MIT',
    author='CERN',
    author_email='info@cc-vary-header.com',
    url='https://github.com/cc-vary-header/cc-vary-header',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'cc-vary-header = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'cc_vary_header_records = cc_vary_header.records:CCVaryHeader',
        ],
        'invenio_base.blueprints': [
            'cc_vary_header = cc_vary_header.theme.views:blueprint',
            'cc_vary_header_records = cc_vary_header.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'cc_vary_header_theme = cc_vary_header.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'cc_vary_header = cc_vary_header.config',
        ],
        'invenio_i18n.translations': [
            'messages = cc_vary_header',
        ],
        'invenio_base.api_apps': [
            'cc_vary_header = cc_vary_header.records:CCVaryHeader',
         ],
        'invenio_jsonschemas.schemas': [
            'cc_vary_header = cc_vary_header.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = cc_vary_header.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
