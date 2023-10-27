from django.shortcuts import render, get_object_or_404
from .forms import CheckoutForm
from .models import History

from django.http import HttpResponseRedirect
from django.urls import reverse

from authentication.models import UserProfile

def show_cart(request):
    cart = request.user.userprofile.cart.all()

    context = {
        "cart": cart,
    }

    return render(request, 'cart.html', context)

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

def show_history(request):
    history = History.objects.filter(user=request.user)

    context = {
        "history": history,
    }

    return render(request, "history.html", context)

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
