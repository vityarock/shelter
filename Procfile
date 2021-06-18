release: python django-admin createsuperuser --database users
release: python ./shelter/manage.py makemigrations
release: python ./shelter/manage.py migrate
release: python ./shelter/manage.py loaddata shelter.json
web: gunicorn shelter.wsgi
