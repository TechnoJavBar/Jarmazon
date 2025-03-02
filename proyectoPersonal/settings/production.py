# production.py

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['localhost','jbarranca.ieshm.org']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',  # O 'django.db.backends.mysql' si usas mysqlclient
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# Configuración del backend de correo para producción
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')