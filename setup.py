#!/usr/bin/env python

from setuptools import setup

setup(
    name='geniatagger-python',
    version='0.2',
    description='Python wrapper for GeniaTagger',
    author='Yen, Tzu-Hsi',
    url='https://github.com/d2207197/geniatagger-python',
    py_modules=['geniatagger'],
    scripts=['geniatagger-server', 'geniatagger-client']
)
