from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls  import url
from django.urls import path
from channels.auth import AuthMiddlewareStack
from socketapp.consumer import CustomConsumer
# from .socketapp import consumer
from channels.security.websocket import AllowedHostsOriginValidator,OriginValidator
application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('',CustomConsumer)
                ]
            )
        )
    )
    # Empty for now (http->django views is added by default)
})