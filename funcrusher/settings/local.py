from funcrusher.settings.settings import *

SECRET_KEY = 'ChangeMe!'

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/funcrusher.db',
    }
}

LOGGING['handlers']['file']['filename'] = '/tmp/funcrusher.log'

STATIC_ROOT = '/tmp/funcrusher_static/'
