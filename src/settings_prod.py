import os
from settings_common import *


DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


# Application

ALLOWED_HOSTS = []


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': os.environ['BLOG_DB_USER'],
        'PASSWORD': os.environ['BLOG_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
