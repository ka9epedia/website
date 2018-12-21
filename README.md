# WebSite

## Image
![website-image](https://user-images.githubusercontent.com/42766115/50330197-ae7bbe80-053d-11e9-9654-161fb8606c17.png)

## Requirement
- Django==2.1.2
- Pillow==5.2.0
- psycopg2==2.7.5
- psycopg2-binary==2.7.5
- Markdown==2.6.9
- martor==1.3.5

## local start
Please create local_setting.py file
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
Type command
<pre>
git clone https://github.com/ka9epedia/website.git
cd website
pip install -r requirements.txt
</pre>
Please create database and run in command line
<pre>
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
</pre>
go [localhost:8000](http://localhost:8000/)
