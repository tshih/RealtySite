
import os

from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SECRET_KEY = 'o&s+uzb4--_h_+!h8g_h-$apdtm)yz&i1s)@nmrac44e(^ml02'

STATIC_URL = '/static/'
STATIC_ROOT = "D:/PythonProjects/ShihsRealty/static"
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'