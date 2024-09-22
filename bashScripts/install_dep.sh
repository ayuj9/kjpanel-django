



# set -e
# set -x
echo "ayushi ayushiaysu"
which python3
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


