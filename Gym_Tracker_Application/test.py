import json
import time
import requests
from progress.bar import ChargingBar
from colorama import Fore, Style

def progress_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            print('❌ Server dosn`t answer!')
            return
        total_iterations = 100 
        progress_bar = ChargingBar('Processing', max=total_iterations)
        
        try:
            for iteration in range(total_iterations):
                time.sleep(0.01)
                progress_bar.next()
        except KeyboardInterrupt:
            progress_bar.finish()
            raise

        progress_bar.finish()
        
        print(f"{Fore.YELLOW}{result[0]}{Style.RESET_ALL}")
        if result[1]:
            print('✅ Test worked succsesfull')
        else:
            print('❌ Test worked badly')
        return result

    return wrapper


@progress_decorator
def signup_test():
    base_url = "http://localhost:8000/auth/signup/"

    user_data = {
        'username': 'testuser3',
        'email': 'testuser@example.com',
        'about': 'This is a test user',
        'password': 'testpassword',
    }

    response = requests.post(base_url, data=user_data)

    if response.status_code == 201:
        print("User created successfully.")
        user_id = response.json().get('user_id')
        print(f"User ID: {user_id}")
    elif response.status_code == 400:
        print("Failed to create a user. Validation errors:")
        print(response.json().get('errors'))
    else:
        print("Failed to creat  e a user. Status code:", response.status_code)


@progress_decorator
def login_test():
    base_url = "http://localhost:8000/auth/login/"

    user_data = {
        'username': 'testuser3',
        'password': 'testpassword',
    }

    response = requests.post(base_url, data=user_data)

    if response.status_code == 200:
        print("User have login successfully.")
        user_id = response.json().get('user_id')
        print(f"User ID: {user_id}")
    elif response.status_code == 401:
        print("Failed to login a user. Validation errors:")
        print(response.json().get('errors'))
    else:
        print("Failed to login a user. Status code:", response.status_code)


@progress_decorator
def create_workout_test():
    base_url = "http://localhost:8000/create_workout/"

    workout_data = {
        'name': 'Upper Body Workout',
        'description': 'A workout focused on upper body exercises',
        'exercises': [1, 2],  # Список ідентифікаторів вправ, які ви хочете пов'язати з цим тренуванням
        'user': 1,
    }

    response = requests.post(base_url, data=workout_data)
    

    if response.status_code == 201:
        print("Workout has been created successfully.")
    elif response.status_code == 400:
        print("Failed to create workout. Validation errors:")
        print(response.json().get('errors'))
    else:
        print("Failed to create a workout. Status code:", response.status_code)


@progress_decorator
def create_workout_data_test():
    base_url = "http://localhost:8000/create_workout_data/"

    workout_data_data = {
            'date': '2023-11-13',
            'user': 1
        }

    response = requests.post(base_url, data=json.dumps(workout_data_data))

    if response.status_code == 201:
        return ("WorkoutData has been created successfully.", True)
    elif response.status_code == 400:
        return ("Failed to create workout-data.", False)
    else:
        return("Failed to create a workout-data.", False)


@progress_decorator
def get_workout_data_last_week_test():
    base_url = "http://localhost:8000/get_weeks_statistic/"

    user_data = {
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkI…WEifQ._3PyfHfvcGlRMHRdJyltlLB87CA8KuSDGjE4EwePVjk',
            'user': 1
    }
    response = requests.post(base_url, data=json.dumps(user_data))

    if response.status_code == 200:
        return (f"Data used successfully. Data: {response.json()}", True)
    elif response.status_code == 400:
        return ("Failed to open workout-data.", False)
    else:
        return ("Failed to open a workout-data.", False)


get_workout_data_last_week_test()