from .base import *



DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PRODUCTION_DB_NAME'),
        'USER': config('PRODUCTION_DB_USER'),
        'PASSWORD': config('PRODUCTION_DB_PASSWORD'),
        'HOST': config('PRODUCTION_DB_HOST')
    }
}
