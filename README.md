# WebSite

## Requirement
- Django==2.1.2
- Pillow==5.2.0
- psycopg2==2.7.5
- psycopg2-binary==2.7.5
- Markdown==2.6.9
- martor==1.3.5

## local start
create local_setting.py
<pre>
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'secret_key'
 
EMAIL_HOST = 'host'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'host_user'
EMAIL_HOST_PASSWORD = 'host_passwor'
EMAIL_USE_TLS = True
 
DEBUG = True
 
ALLOWED_HOSTS = ['*']
  
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

MARTOR_IMGUR_CLIENT_ID = 'client_id'
MARTOR_IMGUR_API_KEY   = 'api_key'
</pre>
create database and run
<pre>
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
</pre>
go [localhost:8000](http://localhost:8000/)
