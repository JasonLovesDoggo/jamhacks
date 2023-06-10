from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass


class Badge(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    ...  # todo extend

    def __str__(self):
        return self.name
