#!/usr/bin/env bash
# Python version set karna
echo "Setting Python Version to 3.10.12"
pyenv install 3.10.12
pyenv global 3.10.12
pip install --upgrade pip
pip install -r requirements.txt
