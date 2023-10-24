from django.shortcuts import render, get_object_or_404
from .models import Katalog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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