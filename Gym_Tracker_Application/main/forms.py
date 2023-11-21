from django import forms

from main.models import Workout, WorkoutData


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'exercises', 'user']


class WorkoutDataForm(forms.ModelForm):
    class Meta:
        model = WorkoutData
        fields = ['date', 'user']
