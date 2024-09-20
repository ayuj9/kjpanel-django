#!/bin/bash



echo "New Venv Starting"

# echo "virtualenv $VIRTUAL_ENV ==  and  $PWD/venv1" 

# source ./tests/venv1/bin/activate
source $(pwd)/tests/venv1/bin/activate


echo "Virtual Environment activated successfully."

pip install --upgrade pip

# pip install -r ./tests/requirements.txt
pip install requests

echo "Venv Virtual Environment activated"

# python ./tests/test.py

echo "test File started"