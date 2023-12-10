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

# @login_required(login_url="authentication:login")
# def choose_book_review_flutter(request):
#     books = Katalog.objects.all()
#     form = ReviewBookForm(request.POST or None)

#     context = {
#         'products': books,
#         'form': form
#     }

#     return JsonResponse(context, safe=False)

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_review = Review.objects.create(
            user = request.user,
            book_review = Katalog.objects.get(pk = data["id"]),
            rating = int(data["rating"]),
            review_message = data["review_message"],
        )

        # new_review = Review(user=user, book_review=book_review, rating=rating, review_message=review_message)
        new_review.save()

        return JsonResponse({"status": "ADDED"}, status=201)
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
    serialized_data = serializers.serialize("json", latest_reviews)
    return HttpResponse(serialized_data, content_type="application/json")

def show_review_flutter(request):
    review = Review.objects.all().order_by("-id")
    serialized_data = serializers.serialize("json", review)
    return HttpResponse(serialized_data, content_type="application/json")