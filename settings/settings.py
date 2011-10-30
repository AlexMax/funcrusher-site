# Django settings for funcrusher project.

import os, sys

# Django project directory.
PROJECT_ROOT = os.path.normpath(__file__ + '/../..') + '/'

# Directory for uploads, sqlite3 databases and other non-code parts of
# the site that are not version controlled.
SITE_ROOT = os.path.normpath(__file__ + '/../../..') + '/'

# We want to put our django apps in their own directory.
sys.path.append(PROJECT_ROOT + 'apps/')

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/New_York'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

DEFAULT_FROM_EMAIL = 'FUNCRUSHER+ <noreply@funcrusherplus.net>'

SITE_ID = 1

USE_L10N = True

STATIC_ROOT = SITE_ROOT + 'static_root/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_ROOT + 'static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT + 'templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'registration',
    'profiles',
    'servers',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamped': {
            'format': '[%(asctime)s] %(levelname)s "%(message)s"',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': SITE_ROOT + 'log/funcrusher.log',
            'formatter': 'timestamped',
        },
    },
    'loggers': {
        'funcrusher.user_login': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}

AUTH_PROFILE_MODULE = 'profiles.profile'

ACCOUNT_ACTIVATION_DAYS = 7

from secret import *
