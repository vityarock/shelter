release: python django-admin createsuperuser --database users
release: python manage.py migrate
web: gunicorn shelter.wsgi
