import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings
from main.db_communicate import get_workout_statistics
from main.forms import WorkoutForm, WorkoutDataForm


@csrf_exempt
def create_workout(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = WorkoutForm(data)
        if form.is_valid():
            workout = form.save()
            return JsonResponse({'message': 'Workout created successfully', 'user_id': workout.id}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def create_workout_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = WorkoutDataForm(data)
        if form.is_valid():
            workout_data = form.save()
            return JsonResponse({'message': 'WorkoutData created successfully', 'user_id': workout_data.id}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def get_workout_data_last_week_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            decoded_token = jwt.decode(data['token'], settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token['user_id']
        except:
            return JsonResponse({'message': 'You are not logined'})
        try:
            workout_data_list = get_workout_statistics(user_id)
            print(workout_data_list)
            return JsonResponse({'message': 'Your profile has found', 'workout_data_list': workout_data_list, 'username': decoded_token['username']},
                                status=200)
        except Exception as err:
            print("Some error")
            return JsonResponse({'message': err}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


