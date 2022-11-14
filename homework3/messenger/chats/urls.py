from django.urls import path

from .views import chat_list, get_chat, create_chat

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('chat', get_chat, name='get_chat'),
    path('chat/create', create_chat, name='create_chat'),
]
