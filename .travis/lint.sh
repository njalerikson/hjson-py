#!/usr/bin/bash

# install dependencies
pip install flake8 flake8-bugbear flake8-builtins flake8-coding flake8-comprehensions flake8-executable isort black

# run flake8 style tests - ignore code complexity checks
flake8 hjson setup.py --extend-ignore=C901,R701,CCR001
# run isort import checks
isort -c -rc hjson setup.py
# run black formatting check
black --quiet --check hjson setup.py
