# Developer Setup

This document will outline how to setup a developer / local environment for the manumissions project.

1) Install python@3.8 or python@3.9 on your local system.
1) Install the latest version of the PostgreSQL database server.
1) Clone the repository to your local environment.
1) Create a Python virtual environment (using your previously installed version of python):
    - `python -m venv ./venv`
1) Activate the virtual environment:
    - `source ./venv/bin/activate` - Unix or OSX based systems
    - `.\venv\bin\Activate.ps1` - Windows
1) After activating the virtual environment install the project requirements.
    - Execute: `pip install -r requirements.txt`
1) Create a `manumissions` database, user, and password in your local PostgreSQL installation:
    * Execute `CREATE USER manumissions;`
    * Execute `ALTER USER manumissions WITH PASSWORD '<choose your password>';`
    * Execute `CREATE DATABASE manumissions WITH OWNER=manumissions;`
1) Create a `.env` file (see the .env.example) and update the properties to match your local system settings.
    * Copy the `.env.example` file and rename it `.env`.
    * Update the settings in your `.env` file to match your local configuration.
        - Be sure to use the database user password from the previous configuration step.
1) Run `python manage.py migrate` to migrate the database tables locally.
1) Run `python manage.py runserver` to start the app server locally.
1) You should be able to connect to the local server at http://127.0.0.1:8000/



Django upgrade to latest as well.
