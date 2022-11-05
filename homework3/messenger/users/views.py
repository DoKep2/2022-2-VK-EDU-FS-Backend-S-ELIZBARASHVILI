from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, ListAPIView

from users.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'name', 'age', 'registration_date')


class UserView(ListAPIView):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()


class SingleUserView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = MyUser.objects.filter(id=self.request.query_params.get('id'))
        return user

    def create_user(self, serializer):
        return serializer.save(user=self.request.data)
