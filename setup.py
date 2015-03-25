#!/usr/bin/env python
#
# Copyright 2013 Stoneopus
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

try:
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

kwargs = {}

version = "0.1.0"

if setuptools is not None:
    # If setuptools is not available, please on your own for dependencies.
    kwargs['install_requires'] = ['psycopg2>=2.5.4']

setup(
    name="tornpg",
    version=version,
    py_modules=["tornpg"],
    author="Mark Gao",
    author_email="gx@stoneopus.com",
    url="https://github.com/markgao/tornpg",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="A lightweight PostgresSQL database adapter wrappered around psycopg2.",
    **kwargs
    )