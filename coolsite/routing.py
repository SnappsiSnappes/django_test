from channels.auth import AuthMiddleware, AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
#*import chat.routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            #*chat.routing.websocket_urlpatterns
        )
    )
})