#!/usr/bin/env python

from setuptools import setup

setup(
    name='geniatagger-python',
    version='0.1',
    description='Python library for GeniaTagger',
    author='OKAMURA Yasunobu',
    url='https://github.com/informationsea/geniatagger-python',
    py_modules=['geniatagger'],
    scripts=['geniatagger-socket']
)
