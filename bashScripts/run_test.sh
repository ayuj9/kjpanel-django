#!/bin/bash

echo "New enviornment Starting"
python3 -m venv .venv1

echo "Env. successfully created"
source .venv1/bin/activate
echo "Virtual Environment activated successfully."


echo "Installing dependencies"
pip install -r ./tests/requirements.txt



echo "test File started"
pytest