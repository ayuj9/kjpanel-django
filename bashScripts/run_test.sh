#!/bin/bash

echo "New enviornment Starting"
python3 -m venv .venv1

echo "Env. successfully created"
source .venv1/bin/activate
echo "Virtual Environment activated successfully."


echo "Installing dependencies"
python3 -m pip install pytest .
pip install requests 



echo "test File started"
pytest