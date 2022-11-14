from django.urls import path

from .views import ChatsView, SingleChatView

urlpatterns = [
    path('', ChatsView.as_view()),
    path('chat', SingleChatView.as_view())
]
