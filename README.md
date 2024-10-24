# manumissions

The manumissions project is is a static~ish site developed and maintained by the Haverford College Library.

### Technology and Organization

This project uses the following technology stack:
    * python - The project development language.
    * Django - The web framework used for APIs and more.
    * PostgreSQL - The database where content is stored.

This project is organized into a number of subdirectories containing the various parts of the project as follows:
    * `catalog` - The database models and migrations for the content stored thusly
    * `manumissions` - The project root, with the global settings, urls, and wsgi configuration.
    * `staticfiles` - The sites static content is served from this folder
    * `templates` - The sites Django templates are located in this folder

Other content that is stored in the root of the project:
    * `.env.example` - Sample `.env` file developers should copy and configure for their specific environment
    * `manage.py` - The Django manage script
    * `requirements.txt` - The project library dependency list
    * `.gitignore` - The standard git ignore file for the project
    * `DEV_SETUP.md` - Developer local setup guide
    * `README.md` - This document

### Digital Ocean Droplet

This project is deployed out to a droplet on the Digital Ocean cloud for its production environment.

The application is deployed to `/srv/manumissions` on the droplet.  The app is owned by `www-data:www-data` on the droplet, user `www-data` is configured with the `/usr/sbin/nologin` shell for security.

The application is hosted by an nginx web server instance running on the droplet as a service which is configured with SSL certs from Let's Encrypt. The application configuration for nginx is located here: `/etc/nginx/sites-available/manumissions`.

The Django app is served by uWSGI which has its configuration here: `/etc/uwsgi/apps-available/manumissions.ini`.  Of note in the configuration the python virtual environment is located here: `/usr/local/lib/python-virtualenv/manumissions`.

A PostgreSQL instance is deployed onto the same droplet which the application is configured to connect to for its database requirements.  Currently PostgreSQL 12.20 is deployed on the droplet.  (XXX: Would it be possible to upgrade this instance to PostgreSQL 17-latest?)
