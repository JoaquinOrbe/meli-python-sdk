#!/usr/bin/env python

import os
from distutils.core import setup

version = '1.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
]

root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'
long_desc = open(root_dir + '/README.md').read()

setup(
    name='meli-python-sdk',
    version=version,
    url='https://github.com/estrategiasdiferenciadas/meli-python-sdk',
    download_url='https://github.com/estrategiasdiferenciadas/meli-python-sdk',
    author='Joaquin Orbe',
    author_email='joaquin_orbe@edsa.com.ar',
    license='The MIT License',
    install_requires=[
        'requests',
    ],
    py_modules=['melipy'],
    description='Mercado Libre Python SDK',
    classifiers=classifiers,
    long_description=long_desc,
    keywords='Mercado Libre SDK',
)
