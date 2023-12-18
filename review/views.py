from django.shortcuts import render
from products.models import Katalog
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from review.models import Review
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from review.forms import ReviewBookForm
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import random

@login_required(login_url="authentication:login")
def show_main(request):
    review = Review.objects.all().order_by("-id")
    context = {
        "review": review
    }
    return render(request, 'review.html', context)

@login_required(login_url="authentication:login")
def choose_book_review(request):
    books = Katalog.objects.all()
    form = ReviewBookForm(request.POST or None)

    context = {
        'products': books,
        'form': form
    }

    return render(request, "choose_book.html", context)

@csrf_exempt
def add_review(request):
    if request.method == "POST":
        user = request.user
        book_review = Katalog.objects.get(pk=request.POST.get("id"))
        rating = request.POST.get("rating")
        review_message = request.POST.get("review_message")

        new_review = Review(user=user, book_review = book_review, rating = rating, review_message = review_message)
        new_review.save()

        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        new_review = Review.objects.create(
            user = User.objects.get(username=data["username"]),
            book_review = Katalog.objects.get(pk = data["id"]),
            rating = int(data["rating"]),
            review_message = data["review_message"],
        )
        
        # new_review = Review(user=user, book_review=book_review, rating=rating, review_message=review_message)
        new_review.save()

        return JsonResponse({"status": "success"}, status=201)
    else:
        return JsonResponse({"status": "Not Found"}, status=404)

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_review(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def get_book_review_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_latest_reviews(request):
    latest_reviews = Review.objects.all().order_by('-id')[:3]
    data = []
    for p in latest_reviews:
        each_data = {
            "image" : p.book_review.Image,
            "fullname" : p.user.userprofile.full_name,
            "BookTitle" : p.book_review.BookTitle,
            "BookAuthor" : p.book_review.BookAuthor,
            "reviewMessage" : p.review_message,
            "rating" : p.rating
        }
        data.append(each_data)

    return HttpResponse(json.dumps(data), content_type="application/json")

def show_review_flutter(request):
    review = Review.objects.all().order_by("-id")
    data = []
    for p in review:
        each_data = {
            "image" : p.book_review.Image,
            "fullname" : p.user.userprofile.full_name,
            "BookTitle" : p.book_review.BookTitle,
            "BookAuthor" : p.book_review.BookAuthor,
            "reviewMessage" : p.review_message,
            "rating" : p.rating
        }
        data.append(each_data)

    return HttpResponse(json.dumps(data), content_type="application/json")

def show_random_book_flutter(request):
    all_books = Katalog.objects.all()
    random_book = random.sample(list(all_books), 3)
    data = []
    for book in random_book :
        each_data = {
            "id": book.id, "BookTitle": book.BookTitle, "BookAuthor": book.BookAuthor, "Image": book.Image, #"ISBN" : book.ISBN, "Year_Of_Publication" : book.Year_Of_Publication, "Publisher" : book.Publisher
        }
        data.append(each_data)

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def show_bookUser_flutter(request):
    data = []
    counter = 1
    if (request.user.pk+1 == 0):
        data1 = Katalog.objects.get(pk=(request.user.pk+1+counter)%100)
        data2 = Katalog.objects.get(pk=(request.user.pk+2+counter)%100)
        data3 = Katalog.objects.get(pk=(request.user.pk+3+counter)%100)
    elif (request.user.pk+2 == 0):
        data1 = Katalog.objects.get(pk=(request.user.pk+1)%100)
        data2 = Katalog.objects.get(pk=(request.user.pk+2+counter)%100)
        data3 = Katalog.objects.get(pk=(request.user.pk+3+counter)%100)
    elif (request.user.pk+3 == 0):
        data1 = Katalog.objects.get(pk=(request.user.pk+1)%100)
        data2 = Katalog.objects.get(pk=(request.user.pk+2)%100)
        data3 = Katalog.objects.get(pk=(request.user.pk+3+counter)%100)
    tmp = []
    tmp.append(data1)
    tmp.append(data2)
    tmp.append(data3)
    for book in tmp :
        each_data = {
            "id": book.id, "BookTitle": book.BookTitle, "BookAuthor": book.BookAuthor, "Image": book.Image, #"ISBN" : book.ISBN, "Year_Of_Publication" : book.Year_Of_Publication, "Publisher" : book.Publisher
        }
        data.append(each_data)
        print(data)
    return JsonResponse(json.dumps(data), safe=False)

