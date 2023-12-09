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