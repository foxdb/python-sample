# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='python-sample',
    version='0.1.0',
    description='Sample Python Project',
    long_description=README,
    author='Ben Schmitt',
    author_email='bens.schmitt@gmail.com',
    url='https://gitlab.com/foxdb/python-sample',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
