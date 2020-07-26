import os
from .default import *

print('Applying development settings')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qd2*_2jc&0vdtrfoum#5p1o3=)$(a7#5_mb)k7k-y9!d6_7)4-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password'
    }
}

# Front End settings
DASHBOARD_TEMPLATE_URL = 'http://localhost:8080'
