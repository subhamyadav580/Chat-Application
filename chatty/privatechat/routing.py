from django.urls import path
from privatechat.consumers import PrivateChatConsumer

websocket_urlpatterns = [
    path('privatechat/chat', PrivateChatConsumer.as_asgi()),
]