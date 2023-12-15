import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Katalog
from authentication.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import BookFilterForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="authentication:login")
def show_katalog(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if user_profile.user_type.casefold() == "writer":
        katalog_list = serializers.serialize('json', Katalog.objects.all())
        katalog_list = serializers.deserialize('json', katalog_list)
        katalog_list = [book.object for book in katalog_list]

        return render(request, 'writer_katalog.html', {'products': katalog_list})

    books = Katalog.objects.all()
    form = BookFilterForm(request.GET)

    if form.is_valid():
        author_name = form.cleaned_data.get("author_name")
        publisher = form.cleaned_data.get("publisher")
        published_year = form.cleaned_data.get("published_year")

        if author_name:
            books = books.filter(BookAuthor__icontains=author_name)

        if publisher:
            books = books.filter(Publisher__icontains=publisher)

        if published_year:
            books = books.filter(Year_Of_Publication=published_year)

    context = {
        'form': form,
        'products': books,
    }

    return render(request, 'katalog.html', context)


@login_required(login_url="authentication:login")
def book_detail(request, book_id):
    book = get_object_or_404(Katalog, id=book_id)
    context = {'book': book}
    if UserProfile.objects.get(user=request.user).user_type.casefold() == "writer":
        return render(request, 'writer_book_detail.html', context)
    return render(request, 'book_detail.html', context)

@csrf_exempt
def add_book(request):
    if request.method == "POST":
        ISBN = request.POST.get('ISBN')
        BookTitle = request.POST.get('BookTitle')
        BookAuthor = request.POST.get('BookAuthor')
        Year_Of_Publication = request.POST.get('Year_Of_Publication')
        Publisher = request.POST.get('Publisher')
        Image = request.POST.get('Image')
        
        new_book = Katalog(ISBN=ISBN, BookTitle=BookTitle, BookAuthor=BookAuthor, Year_Of_Publication=Year_Of_Publication, Publisher=Publisher, Image=Image)
        new_book.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_to_cart(request, book_id, user_id):
    user = request.user.userprofile
    book = get_object_or_404(Katalog, id=book_id)
    user.cart.add(book)
    return redirect('products:show_katalog')

def get_book(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_book_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            isbn = data.get('ISBN')
            title = data.get('BookTitle')
            author = data.get('BookAuthor')
            year = data.get('Year_Of_Publication')
            publisher = data.get('Publisher')
            image_url = data.get('Image')

            new_book = Katalog.objects.create(
                ISBN=isbn,
                BookTitle=title,
                BookAuthor=author,
                Year_Of_Publication=year,
                Publisher=publisher,
                Image=image_url 
            )

            new_book.save()

            return JsonResponse({"status": "success", "message": "Book added successfully"}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

@csrf_exempt
def filter_books(request):
    author_name = request.GET.get('author_name', '')
    publisher = request.GET.get('publisher', '')
    year_of_publication = request.GET.get('year', None)

    books = Katalog.objects.all()
    if author_name:
        books = books.filter(BookAuthor__icontains=author_name)
    if publisher:
        books = books.filter(Publisher__icontains=publisher)
    if year_of_publication:
        books = books.filter(Year_Of_Publication=year_of_publication)

    books_json = serializers.serialize('json', books)
    return JsonResponse(books_json, safe=False)

@csrf_exempt
def add_to_cart_flutter(request, book_id, user_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            user = UserProfile.objects.get(id=user_id)
            book = get_object_or_404(Katalog, id=book_id)
            user.cart.add(book)
            return JsonResponse({"status": "success", "message": "Book added successfully"}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)