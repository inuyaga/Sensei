# chat/routing.py
from django.conf.urls import url
from aplicaciones.chat import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]