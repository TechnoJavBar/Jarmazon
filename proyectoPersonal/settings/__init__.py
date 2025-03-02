# settings/__init__.py
from decouple import config

if config('DJANGO_ENV')=='production':
    print('en modo produccion....')
    from .production import *
else:
    print('en modo local.....')
    from .local import *