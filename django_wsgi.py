import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.prod'

path = '/srv/www/funcrusher/django/funcrusher'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
