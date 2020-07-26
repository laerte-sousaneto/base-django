import os
import django_heroku

from .default import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

print('Applying production settings')

SECRET_KEY = os.environ['SECRET_KEY']
DASHBOARD_TEMPLATE_URL = os.environ['DASHBOARD_TEMPLATE_URL']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# This application uses postgres database but Heroku takes care of production settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#     }
# }

django_heroku.settings(locals())
