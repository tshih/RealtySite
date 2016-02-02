import os
from .base import *
from django.utils.crypto import get_random_string

def generate_secret_key(filename):

	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	secret_key = "SECRET_KEY = \'" + crypto.get_random_string(50, chars) + "\'"
	fd = open(filename, 'w')
	fd.write(secret_key)
	fd.close()

try:
    from .secret_key import *
except ImportError:
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from secret_key import *

STATIC_ROOT = "ShihsRealty/staticfiles"