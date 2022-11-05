from rest_framework import serializers
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.generics import ListCreateAPIView, get_object_or_404, ListAPIView

from chats.models import Chat
from users.models import MyUser


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'name', 'data', 'user')


class ChatsView(ListAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class SingleChatView(ListCreateAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        chat = Chat.objects.filter(id=self.request.query_params.get('id'))
        return chat

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        user = MyUser(id=self.request.data.get('user'))
        return serializer.save(user=user)
