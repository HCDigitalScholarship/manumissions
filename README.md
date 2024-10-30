# manumissions

The manumissions project is is a static~ish site developed and maintained by the Haverford College Library.

### Technology and Organization

This project uses the following technology stack:
* python - The project development language.
* Django - The web framework used for APIs and more.
* PostgreSQL - The database where content is stored.

This project is organized into a number of subdirectories containing the various parts of the project as follows:
* `catalog` - The database models and migrations for the content stored thusly
    - The `management` folder contains a set of scripts and csv files for ???
    - The `migrations` folder contains the set of database migrations
    - The `static` folder contains the static content for the catalog portion of the site
    - The `templates` folder contains the Django templates
        - Most of the other templates use `catalog/templates/base_generic.html` as a base
    - The `tests` folder contains unit tests for the catalog portion of the site
* `manumissions` - The project root, with the global settings, urls, and wsgi configuration.
* `staticfiles` - The sites static content is served from this folder
    - The `admin` folder contains the Django admin site
    - The `css` folder contains the site cascading stylesheets
* `templates` - The sites Django templates are located in this folder
    - The `registration` folder contains templates for user auth operations on the site such as login, logout, and password reset.

Other content that is stored in the root of the project:
* `README.md` - This document
* `DEV_SETUP.md` - Developer local setup guide
* `manage.py` - The Django manage script
* `requirements.txt` - The project library dependency list
* `.env.example` - Sample `.env` file developers should copy and configure for their specific environment
* `.gitignore` - The standard git ignore file for the project

### Digital Ocean Droplet

This project is deployed out to a droplet on the Digital Ocean cloud for its production environment.

The application is deployed to `/srv/manumissions` on the droplet.  The app is owned by `www-data:www-data` on the droplet, user `www-data` is configured with the `/usr/sbin/nologin` shell for security.

The application is hosted by an nginx web server instance running on the droplet as a service which is configured with SSL certs from Let's Encrypt. The application configuration for nginx is located here: `/etc/nginx/sites-available/manumissions`.

The Django app is served by uWSGI which has its configuration here: `/etc/uwsgi/apps-available/manumissions.ini`.  Of note in the configuration the python virtual environment is located here: `/usr/local/lib/python-virtualenv/manumissions`.

A PostgreSQL instance is deployed onto the same droplet which the application is configured to connect to for its database requirements.  Currently PostgreSQL 12.20 is deployed on the droplet.
(XXX: Would it be possible to upgrade this instance to PostgreSQL 17-latest?)


### Maintenance Schedule

Site maintenance should be scheduled for roughly every 3 months.  In addition a review should be performed in the case any zero day security vulnerabilities are discovered in the libraries and utilities used by the site.  This review should include all libraries in the `requirements.txt` file in addition included script libraries like jQuery (e.g. referenced in `catalog/templates/base_generic.html`) included in the templates should also be reviewed and upgraded according to this schedule.
SSL certificates for the production site should be set to renew using certbot every 90 days.
The droplet should be scheduled for backups monthly or whenver the site undergoes a data update or maintenance schedule.  This will allow restoration of the site in case of disruption.
