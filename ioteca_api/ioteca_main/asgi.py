"""
ASGI config for ioteca_main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ioteca_main.settings')


print("Este es mi commit a asgi.py - Valentin Arenaza")

application = get_asgi_application()
