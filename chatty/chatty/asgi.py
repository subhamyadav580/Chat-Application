import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
import privatechat.routing
from chat.routing import websocket_urlpatterns
from privatechat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      chat.routing.websocket_urlpatterns +
      privatechat.routing.websocket_urlpatterns
    )
  )
})