from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from authentication.forms import RegisterForm
from authentication.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get("next")
            if next_page is None:
                response = redirect("main:show_main")
            else:
                response = redirect(next_page)
            response.set_cookie("user_logged_in", user)
            return response
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again.")
    context = {}
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, "login.html", context)


@csrf_exempt
def login_mobile(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({
                "username": user.username,
                "fullname": user.userprofile.full_name,
                "id": user.id,
                "type": user.userprofile.user_type,
                "status": True,
                "message": "Login successful!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed. Account is deactivated."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed. Try again."
        }, status=401)


@csrf_exempt
def logout_mobile(request):
    username = request.user.username
    try:
        logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout successful!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    context = {"form": form}
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, "register.html", context)


@csrf_exempt
def register_mobile(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if User.objects.filter(username=data["username"]).exists():
            return JsonResponse({
                "status": False,
                "message": "Register failed. Account with that username already exists."
            }, status=401)

        if data["password1"] != data["password2"]:
            return JsonResponse({
                "status": False,
                "message": "Register failed. The two passwords don't match."
            }, status=401)
        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password1"]
        )
        user.save()

        user_profile = UserProfile.objects.create(
            user=user,
            full_name=data["full_name"].strip(),
            user_type=data["user_type"].strip(),
        )
        user_profile.save()
        return JsonResponse({
            "status": True,
            "message": "Register successful"
        }, status=201)
    else:
        return JsonResponse({
            "status": False,
            "message": "Register failed. Use POST method."
        }, status=401)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('user_logged_in')
    return response
