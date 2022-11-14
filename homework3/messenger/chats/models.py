from django.db import models

from users.models import MyUser


class Chat(models.Model):
    name = models.CharField(max_length=21)
    data = models.TextField()
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL, verbose_name="user_id")
