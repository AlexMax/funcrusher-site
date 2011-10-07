from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SITE_ROOT + 'db/devel.db',
    }
}

DEBUG = True
TEMPLATE_DEBUG = True
