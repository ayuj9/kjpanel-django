



# set -e
# set -x

pip install --upgrade pip


if [ -f "requirements.txt" ]; then
    echo "Installing dependencies"
    pip install -r requirements.txt
    echo "All dependencies installed"

else 
   echo "No requirements.txt file found"   
fi    

echo "Dependencies have been successfully installed."   




