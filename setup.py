#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'salesforce_oauth_request',
]

requires = [
    'requests>=2.2.1',
    'six>=1.10.0',
]

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')
with open('LICENSE') as f:
    license = f.read()

setup(
    name='salesforce-oauth-request-yplan',
    version='1.1.1',
    description='Util package to drive Salesforce Oauth Web flow for testing.',
    long_description=readme + "\n\n" + history,
    author='Scott Persinger',
    author_email='scottp@heroku.com',
    url='https://github.com/YPlan/salesforce-oauth-request',
    maintainer='YPlan',
    maintainer_email='julius@yplanapp.com',
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)
