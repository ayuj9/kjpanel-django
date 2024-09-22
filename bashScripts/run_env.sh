#!/bin/bash

ls


VENV_DIR="myenv"

if [ ! -d "$VENV_DIR" ]; then
   echo "Virtual Enviornment not created"
   python3 -m venv $VENV_DIR
else 
   echo "Virtual Environment already exists"   
fi



if [ -d "$VENV_DIR" ]; then
    echo "Activating virtual environment..."
    source myenv/bin/activate


    # Check if activation was successful
    if [ "$VIRTUAL_ENV" == "$PWD/$VENV_DIR" ]; then
        echo "Virtual Environment activated successfully."
    else
        echo "Failed to activate Virtual Environment."
    fi
else
    echo "Virtual Environment directory does not exist. Activation failed."
    exit 1
fi

pip install --upgrade pip


if [ -f "requirements.txt" ]; then
    echo "Installing dependencies"
    pip install -r requirements.txt
    echo "All dependencies installed"
    python manage.py runserver

else 
   echo "No requirements.txt file found"   
fi    

echo "Dependencies have been successfully installed."   


