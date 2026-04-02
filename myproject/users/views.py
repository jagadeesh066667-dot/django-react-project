from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# 🔐 Home
@login_required
def home(request):
    return render(request, 'home.html')


# 📝 Register
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'Registered successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


# 🔑 Login
@csrf_exempt   # 🔥 VERY IMPORTANT
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login success'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# 🚪 Logout
@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})