#!/usr/bin/env python3
from setuptools import setup, find_packages
from salplot import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='salplot',
    version=__version__,
    description='Salmon Input/Output Tool',
    long_description=readme,
    author='M. Uemoto',
    author_email='',
    url='https://github.com/uemoto1/salplot',
    license=license,
    packages=find_packages(),
    istrall_requires=[
        'numpy>=1.15.0',
        'scipy>=1.1.0',
        'matplotlib>=2.2.2',
        'Vapory>=0.1.1',
    ],
)
