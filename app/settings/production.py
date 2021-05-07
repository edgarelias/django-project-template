"""
Django Production settings to build other settings files upon.
Extends from common.py
For more information on this file, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from .common import *

DEBUG = False

SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

DATABASES['default'] = env.db('DATABASE_URL')

# SECURITY
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')   # This tells Django to trust the X-Forwarded-Proto header that comes from our proxy, and any time its value is 'https', then the request is guaranteed to be secure
SECURE_SSL_REDIRECT = True                                      # The SecurityMiddleware redirects all non-HTTPS requests to HTTPS
SESSION_COOKIE_SECURE = True                                    # The cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection
CSRF_COOKIE_SECURE = True                                       # The cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection
SECURE_HSTS_SECONDS = 60                                        # The SecurityMiddleware sets the HTTP Strict Transport Security header on all responses that do not already have it.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True                           # The SecurityMiddleware adds the includeSubDomains directive to the HTTP Strict Transport Security header. It has no effect unless SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_HSTS_PRELOAD = True                                      # The SecurityMiddleware adds the preload directive to the HTTP Strict Transport Security header. It has no effect unless SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_CONTENT_TYPE_NOSNIFF = True                              # The SecurityMiddleware sets the X-Content-Type-Options: nosniff header on all responses that do not already have it.
X_FRAME_OPTIONS = 'DENY'

# ADMIN PAGE URL
ADMIN_URL = env('DJANGO_ADMIN_URL')