#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.append(os.path.join(os.path.dirname(__file__), 'plushcap'))


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'requests',
]

test_requirements = [
    'requests',
]

setup(
    name='plushcap',
    version='0.2.1',
    description='Plushcap monitors websites and alerts people via text or phone call if there is a problem.',
    long_description=readme + '\n\n' + history,
    author='Matt Makai',
    author_email='mmakai@twilio.com',
    url='https://github.com/makaimc/plushcap',
    packages=[
        'plushcap',
    ],
    package_dir={'plushcap':
                 'plushcap'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='plushcap',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
