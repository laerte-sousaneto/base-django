# -*- coding: utf-8 -*-
import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOP')
print('Environment: {}'.format(ENVIRONMENT))

try:
    if ENVIRONMENT == 'PRODUCTION':
        from .production import *
    elif ENVIRONMENT == 'DEVELOP':
        from .develop import *
except ImportError:
    pass