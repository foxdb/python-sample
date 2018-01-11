# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-sample',
    version='0.1.0',
    description='Sample Python Project',
    long_description=readme,
    author='Ben Schmitt',
    author_email='bens.schmitt@gmail.com',
    url='https://gitlab.com/foxdb/python-sample',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
