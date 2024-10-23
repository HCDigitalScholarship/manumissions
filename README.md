# manumissions

The manumissions project is....


### Digital Ocean Droplet

Python app is deployed to `/srv/manumissions`:
    *** App has local changes to `catalog/models.py` on production
    owned by `www-data:www-data` user with `/usr/sbin/nologin`***
App is deployed with nginx web server:
    configuration at `/etc/nginx/sites-available/manumissions`
    *** this has configuration settings for using letsencrypt already!?!
uWSGI is used as the python app server (pretty common):
    configuation at `/etc/uwsgi/apps-available/manumissions.ini`
    prod venv `/usr/local/lib/python-virtualenv/manumissions`
postgeresql server is on the samehost (postgres user)
    manumissions database (localhost:5432)
    no pg_admin installed
