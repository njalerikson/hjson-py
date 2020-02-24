# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import find_packages, setup

with open("README.rst", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="hjson",
    version="3.0.1",
    description="Hjson, a user interface for JSON.",
    long_description=LONG_DESCRIPTION,
    keywords="json comments configuration",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Academic Free License (AFL)",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author="Christian Zangl",
    author_email="laktak@cdak.net",
    url="http://github.com/hjson/hjson-py",
    license="MIT License",
    packages=find_packages("."),
    entry_points={"console_scripts": ["hjson = hjson.tool:main"]},
)
