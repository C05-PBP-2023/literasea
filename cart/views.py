from django.shortcuts import render
from .forms import CheckoutForm
from .models import History
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
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

def get_cart_json(request):
    cart = request.user.userprofile.cart.all()
    return HttpResponse(serializers.serialize('json', cart))

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
def remove_book_from_cart_ajax(request, id):
    if request.method == "POST":
        book = request.user.userprofile.cart.get(id=id)

        request.user.userprofile.cart.remove(book)

        return HttpResponse(b"OK", status = 200)
    
    return HttpResponseNotFound()
