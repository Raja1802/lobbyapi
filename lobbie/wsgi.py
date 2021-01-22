"""
WSGI config for lobbie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
import os
from whitenoise import WhiteNoise

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lobbie.settings')
django.setup()
application = get_wsgi_application()
application = WhiteNoise(application)