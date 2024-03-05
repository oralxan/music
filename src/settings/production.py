from .base import *



DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : config('PRODUCTION_DB_NAME'),
        'USERNAME' : config('PRODUCTION_DB_USERNAME'),
        'PASSWORD' : config('PRODUCTION_DB_PASSWORD'),
        'HOST':config('PRODUCTION_DB_HOST')
    }
}
#ffv