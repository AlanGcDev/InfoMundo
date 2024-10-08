#!/bin/bash
echo "Building the project..."
/opt/vercel/python3/bin/python3 -m pip install --upgrade pip
/opt/vercel/python3/bin/python3 -m pip install -r requirements.txt

echo "Make migrations..."
/opt/vercel/python3/bin/python3 manage.py makemigrations
/opt/vercel/python3/bin/python3 manage.py migrate

echo "Collect static..."
/opt/vercel/python3/bin/python3 manage.py collectstatic --noinput --clear