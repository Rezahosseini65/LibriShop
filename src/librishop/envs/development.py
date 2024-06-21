from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
    'debug_toolbar',
]+INSTALLED_APPS

INTERNAL_IPS = [
    "0.0.0.0",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'librishop',
        'USER': 'librishop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}

