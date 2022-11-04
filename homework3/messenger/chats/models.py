from django.db import models


class Chat():
    # name = models.CharField(max_length=20)
    # data = models.TextField()

    def __init__(self, name, data):
        self.name = name
        self.data = data
