from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from authentication.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt

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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({
                "username": user.username,
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


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('user_logged_in')
    return response
