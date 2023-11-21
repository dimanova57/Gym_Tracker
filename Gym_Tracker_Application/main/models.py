from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.CharField(max_length=512)
    password = models.CharField("password", max_length=512)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Exercise(models.Model):
    description = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=128)


class Workout(models.Model):  # Workout - it`s group of exercise
    description = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    exercises = models.ManyToManyField(Exercise, related_name='workouts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class WorkoutData(models.Model):  # TODO не забути видалити - Це інфа коли та як ти займався
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
