#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from codecs import open
from setuptools import setup, find_packages
try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger
    logger.warn("Wheel is not available, disabling bdist_wheel hook")

# TODO: Confirm this is the right version number you want and it matches your
# HISTORY.rst entry.
VERSION = '0.1.11'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

# TODO: Add any additional SDK dependencies here
DEPENDENCIES = []

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='appservice-kube',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools App Service on Kubernetes Extension',
    # TODO: Update author and email, if applicable
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    # TODO: consider pointing directly to your source code instead of the generic repo
    url='https://github.com/Azure/azure-cli-extensions/tree/main/src/appservice-kube',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    scripts=['azext_appservice_kube/getfunctionsjson.sh'],
    package_data={'azext_appservice_kube': ['azext_metadata.json',
                                            'resources/LinuxFunctionsStacks.json',
                                            'resources/WindowsFunctionsStacks.json',
                                            'resources/WebappRuntimeStacks.json']},
)
