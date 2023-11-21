import json
from django.http import JsonResponse
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from werkzeug.security import generate_password_hash
import jwt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .login_service import authenticate_user


@csrf_exempt  # @csrf_exempt - це один із можливих способів це зробити, але, як я вже зазначив, слід бути обережним і
# ретельно аналізувати потенційні ризики.
def signup_view(request):
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))
        form = SignUpForm(data)
        if form.is_valid():  # form.is_valid - Чи заповнена та правильна форма
            password = form.cleaned_data['password']
            hashed_password = generate_password_hash(password)
            user = form.save(commit=False)  # commit=False - створює об`єкт, але не зберігає в db
            user.password = hashed_password
            user.save()  # Записуємо юзера в bd

            return JsonResponse({'message': 'User created successfully', 'user_id': user.id}, status=201)
        else:
            errors = form.errors.as_json()  # на формі є встроєні ерори, якщо вони виникають то вони є, якщо ні то None
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            user = authenticate_user(username, password)
        except:
            return JsonResponse({'message': 'Your password or name is incorrect'}, status=200)


        if user:
            payload = {
                'user_id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            return JsonResponse({'message': 'Login successful', 'token': token}, status=200)
        else:
            return JsonResponse({'message': 'Invalid login credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
