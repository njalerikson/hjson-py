#!/usr/bin/env python
from __future__ import with_statement

import os
import re

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
    long_description = f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    path = os.path.join(os.path.dirname(__file__), package, "__init__.py")
    with open(path, "rb") as f:
        init_py = f.read().decode("utf-8")
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="hjson",
    author="Christian Zangl",
    author_email="laktak@cdak.net",
    version=get_version("hjson"),
    url="http://github.com/hjson/hjson-py",
    description="Hjson, a user interface for JSON.",
    long_description=long_description,
    packages=find_packages("."),
    keywords="json comments configuration",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Academic Free License (AFL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    scripts=["bin/hjson", "bin/hjson.cmd"],
)
