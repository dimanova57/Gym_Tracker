from django.urls import path

from main.views import create_workout, create_workout_data, get_workout_data_last_week_view

urlpatterns = [
    path('create_workout/', create_workout, name='create_workout'),
    path('create_workout_data/', create_workout_data, name='create_workout_data'),
    path('get_weeks_statistic/', get_workout_data_last_week_view, name='get_workout_data_last_week_view'),
]
