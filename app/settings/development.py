"""
Django Development settings to build other settings files upon.
Extends from common.py
For more information on this file, see
https://docs.djangoproject.com/en/3.0/ref/settings/
Configures:
- DEBUG (enables handy features like full tracebacks in your browser)
- ALLOWED HOSTS
- CACHES
"""
from .common import *

DEBUG = True

ADMIN_URL = 'admin/'


# ALLOWED HOSTS
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}