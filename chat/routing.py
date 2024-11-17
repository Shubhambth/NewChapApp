from django.urls import path
from .consumers import *


websocket_urlpattern = [
    path("ws/chatroom/<chatroom_name>",ChatroomConsumer.as_asgi())
]