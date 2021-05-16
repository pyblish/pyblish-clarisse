#!/usr/bin/env python
# coding=utf-8
'''
Author: zuokangbo
Date: 2021-05-16 14:34:36
'''
"""This setup script packages pyblish-clarisse."""

# Import built-in modules
import importlib
import os

# Import third-party modules
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = os.path.abspath("pyblish_clarisse/version.py")
version_mod = importlib.import_module("pyblish_clarisse.version")
version = version_mod.version

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="pyblish-clarisse",
    version=version,
    packages=find_packages(),
    url="https://github.com/pyblish/pyblish-clarisse",
    license="LGPL",
    author="Pyblish contributors",
    author_email="me@mottosso.com",
    description="Pyblish for clarisse.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=classifiers,
    install_requires=[
        "pyblish_base>=1.2.1",
        "pyblish_lite>=0.8.0",
    ]
)
