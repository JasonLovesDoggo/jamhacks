from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    ...  # todo extend

    def __str__(self):
        return self.name
    

class Quest(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    time = models.IntegerField(default=0)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def __str__(self):
        return self.name


class Date(models.Model):
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date


class CoreUser(AbstractUser):
    bio = models.CharField(max_length=100, blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    badges = models.ManyToManyField(Badge, blank=True)
    dates_exercised = models.ManyToManyField(Date, blank=True)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Doctor(models.Model):
    """
    A doctor is a user who can view the progress of their patients.

    You can view all the exercises that the doctor has created by querying the LogEntry model.
    """
    user = models.OneToOneField(CoreUser, on_delete=models.CASCADE, primary_key=True)
    patients = models.ManyToManyField(CoreUser, related_name='patients', blank=True)



    def __str__(self):
        return self.user.username