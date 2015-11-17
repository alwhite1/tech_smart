#/usr/bin/python
# -*- coding: utf-8 -*-
"""
WSGI config for tech_smart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os, sys
dn = os.path.dirname
DJANGO_PROJECT_ROOT = os.path.abspath( dn(dn(__file__)) )
sys.path.append( DJANGO_PROJECT_ROOT )
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_smart.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()