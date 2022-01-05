"""
ASGI config for bookstoreapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import django
import os
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstoreapi.settings')
# django.setup()

application = get_asgi_application()

ws_patterns = [
      path('ws/chat/<str:room_name>',ChatConsumer.as_asgi() )
]

application = ProtocolTypeRouter({
  'websocket': URLRouter(ws_patterns),
  # We will add WebSocket protocol later, but for now it's just HTTP.
})
