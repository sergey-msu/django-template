from settings_common import *


DEBUG = True

SECRET_KEY = 'abc123'


# Application

ALLOWED_HOSTS = ['127.0.0.1']


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'serge_msu',
        'PASSWORD': 'spmathf123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
