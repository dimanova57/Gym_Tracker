from django.urls import path

from main.views import create_workout
from .views import signup_view, login_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]
