import json
from django.shortcuts import render
from django.contrib.auth.models import User
import authentication
from .forms import CheckoutForm
from .models import History
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse

@csrf_exempt
@login_required(login_url="authentication:login")
def show_cart(request):
    cart = request.user.userprofile.cart.all()

    form = CheckoutForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        history = form.save(commit=False)
        history.user = request.user
        
        form.save()

        for book in request.user.userprofile.cart.all():
            history.buku.add(book)
            request.user.userprofile.owned_books.add(book)
            request.user.userprofile.cart.remove(book)

        return HttpResponse(b"OK", status=200)

    context = {
        "cart": cart,
        "form": form,
    }

    return render(request, 'cart.html', context)

@login_required(login_url="authentication:login")
def checkout_cart_ajax(request):
    form = CheckoutForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        history = form.save(commit=False)
        history.user = request.user
        
        form.save()

        for book in request.user.userprofile.cart.all():
            history.buku.add(book)
            request.user.userprofile.owned_books.add(book)
            request.user.userprofile.cart.remove(book)

        return HttpResponse(b"OK", status=200)
    
    return render(request, "cart.html", {"form": form})

@csrf_exempt
def checkout_cart_flutter(request):
    if request.method == "POST":

        data = json.loads(request.body)

        # print(data)

        # print(History.objects.filter(user=request.user)[0].buku.all())

        new_history = History.objects.create(
            user = request.user,
            nama = data["nama"],
            alamat = data["alamat"],
        )

        for book in request.user.userprofile.cart.all():
            new_history.buku.add(book)
            request.user.userprofile.owned_books.add(book)
            request.user.userprofile.cart.remove(book)

        new_history.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
            

def get_cart_json(request):
    cart = request.user.userprofile.cart.all()
    return HttpResponse(serializers.serialize('json', cart), content_type="application/json")

def get_cart_json_by_user_id(request, id):
    user = User.objects.filter(id=id)[0]
    cart = user.userprofile.cart.all()

    return HttpResponse(serializers.serialize('json', cart), content_type="application/json")

@login_required(login_url="authentication:login")
def checkout_cart(request):
    form = CheckoutForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        history = form.save(commit=False)
        history.user = request.user
        
        form.save()

        for book in request.user.userprofile.cart.all():
            history.buku.add(book)
            request.user.userprofile.owned_books.add(book)
            request.user.userprofile.cart.remove(book)

        return HttpResponseRedirect(reverse('cart:show_cart'))
    
    return render(request, "checkout.html", {"form": form})

@login_required(login_url="authentication:login")
def show_history(request):
    history = History.objects.filter(user=request.user)

    context = {
        "history": history,
    }

    return render(request, "history.html", context)

def get_history_json(request):
    history = History.objects.all()

    return HttpResponse(serializers.serialize('json', history), content_type="application/json")

@login_required(login_url="authentication:login")
def show_owned(request):
    owned = request.user.userprofile.owned_books.all()

    context = {
        "owned": owned,
    }

    return render(request, "display_owned.html", context)

def remove_book_from_cart(request, book_id):
    book = request.user.userprofile.cart.get(id=book_id)

    request.user.userprofile.cart.remove(book)

    return HttpResponseRedirect(reverse('cart:show_cart'))

@csrf_exempt
def remove_book_from_cart_flutter(request, user_id, book_id):
    user = User.objects.filter(id=user_id)[0]
    book = user.userprofile.cart.get(id=book_id)

    user.userprofile.cart.remove(book)

    return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def remove_book_from_cart_ajax(request, id):
    if request.method == "POST":
        book = request.user.userprofile.cart.get(id=id)

        request.user.userprofile.cart.remove(book)

        return HttpResponse(b"OK", status = 200)
    
    return HttpResponseNotFound()
