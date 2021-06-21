#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

echo "Enter host:port (press Enter for use 0.0.0.0:8000):"
read host

if [ -z "$host" ]
then
      echo "Using default"
      python3 manage.py runserver 0.0.0.0:8000
else
      python3 manage.py runserver "$host"
fi
