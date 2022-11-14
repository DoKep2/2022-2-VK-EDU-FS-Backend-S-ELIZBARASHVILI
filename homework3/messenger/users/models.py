from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    registration_date = models.DateTimeField(auto_now_add=True)
