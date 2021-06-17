release: python ./shelter/manage.py migrate
release: python ./shelter/manage.py loaddata shelter.json
web: gunicorn shelter.wsgi
#web: python manage.py runserver 0.0.0.0:$PORT
