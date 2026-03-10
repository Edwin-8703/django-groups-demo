from .base import *
import dj_database_url
import os

DEBUG = False
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://edwin-django-user-groups.up.railway.app']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}