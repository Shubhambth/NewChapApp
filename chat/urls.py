from django.urls import path 
from . import views

urlpatterns = [
    path('chat/',views.chat,name='chat'),
    path('chat/<username>', views.get_or_create_chatroom,name="start-chat"),
    path('chat/room/<chatroom_name>',views.chat,name="chatroom"),
   
]
