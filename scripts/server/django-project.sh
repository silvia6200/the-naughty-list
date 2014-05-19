#!/bin/bash

# Move to server to set up Django
mkdir -p $SERVER;
cd $SERVER;

echo "django
djangorestframework
south
ipython" > requirements.txt;

# Set up Python Package Management
. $SCRIPTS/server/ppm.sh;

# Create the initial project structure
mkdir -p project;
django-admin.py startproject project .;

echo "
venv
*.pyc
*.pyo
*.sqlite3
" > .gitignore

echo "Server Commands
===============

This system makes use of virtualenv and pip to ensure isolated environments. For more information on why,
see https://virtualenv.pypa.io/en/latest/virtualenv.html.

Assuming you have run setup.sh or that your system is ready to run, firstly activate your virtual environment
from the server directory by running:

    . venv/bin/activate

You will then see in the bottom left of your terminal (venv)/path/to/server. This means the python environment
is isolated and you can now install packages without corrupting the global package space. The libraries associated
with the project should already be available, mainly django, so you can run commands from the server root as
normal:

    ./manage.py (runserver|test|syncdb|migrate)

and so on.

To leave your virtual environment run:

    deactivate
" > README.md
