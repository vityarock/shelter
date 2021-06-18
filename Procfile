release: python django-admin createsuperuser --database users
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py loaddata shelter.json
web: gunicorn shelter.wsgi
