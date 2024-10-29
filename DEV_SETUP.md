# Developer Setup

This document will outline how to setup a developer / local environment for the manumissions project.

1) Install git source control if your system does not already have it installed.
1) Install python@3.13 on your local system.
    - Ensure that your python installation is on your path.
1) Install the latest version of the PostgreSQL database server.
1) Clone the repository to your local environment.
    - `git clone ...`
1) Create a Python virtual environment (using your previously installed version of python):
    - `python3 -m venv ./venv` - Unix or OSX based systems
    - `python -m venv .\venv` - Windows
1) Activate the virtual environment:
    - `source ./venv/bin/activate` - Unix or OSX based systems
    - `.\venv\bin\Activate.ps1` - Windows
1) After activating the virtual environment install the project requirements.
    - Execute: `pip install -r requirements.txt`
1) Create a `manumissions` database, user, and password in your local PostgreSQL installation:
    * Connect to the database using the `psql` command.
    * Execute `CREATE USER manumissions;`
    * Execute `ALTER USER manumissions WITH PASSWORD '<choose your password>';`
    * Execute `CREATE DATABASE manumissions WITH OWNER=manumissions;`
1) Create a `.env` file (see the .env.example) and update the properties to match your local system settings.
    * Copy the `.env.example` file and rename it `.env`.
    * Update the settings in your `.env` file to match your local configuration.
        - Create a secret key that is unique to your system, using a phrase or otherwise.
        - Be sure to use the database host and port configured for your local setup.
        - Be sure to use the database name, user, and user password from the previous configuration step.
1) Execute the database table migrations.
    * Run `python manage.py migrate` to migrate the database tables locally.  This will create a series of empty tables the project requires.
1) Run `python manage.py runserver` to start the app server locally.
1) You should be able to connect to the local server at http://127.0.0.1:8000/
    * Verify that the site is being served correctly.
