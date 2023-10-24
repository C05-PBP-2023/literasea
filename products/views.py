from django.shortcuts import render, get_object_or_404
from .models import Katalog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from authentication.models import UserProfile
from django.shortcuts import redirect

# Create your views here.
def show_katalog(request):
    books = Katalog.objects.all()

    context = {
        'products': books,
    }

    return render(request, "katalog.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Katalog, id=book_id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)

def add_book(request, book_id, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    book = get_object_or_404(Katalog, id=book_id)
    user.cart.add(book)
    return redirect('products:show_katalog')