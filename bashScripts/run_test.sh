#!/bin/bash

echo "New enviornment Starting"
python3 -m venv .venv1

echo "Env. successfully created"
source .venv1/bin/activate
echo "Virtual Environment activated successfully."


echo "Installing dependencies"
pip install -r ./tests/requirements.txt


echo "Starting test execution using pytest"
pytest -s
if [ $? -eq 0 ]; then
  echo "Tests ran successfully"
else
  echo "Error running tests"
  exit 1
fi