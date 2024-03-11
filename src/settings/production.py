from .base import *



DEBUG = False

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clijfhwk',
        'USER': 'clijfhwk',
        'PASSWORD': 'exv_NeTaLsQd4JfxNSOrlp8fjUGlcOlU',
        'HOST': 'floppy.db.elephantsql.com'
=======
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'production.sqlite3',
>>>>>>> 38d4043f7ef516f13e0608375a209b001f6f7ed2
    }
}

