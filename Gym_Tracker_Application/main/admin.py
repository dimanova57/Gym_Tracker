from django.contrib import admin

# Register your models here. Hello world

from django.contrib import admin
from .models import Workout, Exercise, User, WorkoutData


admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(User)
admin.site.register(WorkoutData)
