from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from authentication.forms import RegisterForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect(request.GET.get("next"))
            response.set_cookie("user_logged_in", user)
            return response
        else:
            messages.info(request, "Sorry, incorrect username or password. Please try again.")
    context = {}
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, "login.html", context)
        
    
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show_main')
    context = {"form":form}
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, "register.html", context)
    
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('user_logged_in')
    return response

