#!/usr/bin/bash

# install dependencies
pip install coverage pytest

# run test suite
coverage run --source=hjson -m pytest hjson/tests
# get coverage
coverage report -m
