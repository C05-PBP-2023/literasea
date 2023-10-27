from django.shortcuts import render
from products.models import Katalog
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from review.models import Review
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import ReviewBookForm
# from django.contrib.auth.models import User
@login_required(login_url="authentication:login")
def show_review(request):
    review = Review.objects.all()
    context = {
        "review" : review
    }

    return render(request, "review.html", context)


@login_required(login_url="authentication:login")
def pilih_buku(request, id):
    buku = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", buku), content_type="application/json")

@login_required(login_url="authentication:login")
@csrf_exempt
def review_book(request):
    if request.method == 'POST':
        user_login = request.user
        rating = request.POST.get("rating")
        book_review = Katalog.objects.get(pk=request.POST.get("id"))
        review_message = request.POST.get("review_message")

        print(user_login,book_review,rating,review_message)
        new_review = Review(user_login = user_login, book_review = book_review, rating = rating, review_message = review_message)
        new_review.save()

        return HttpResponse(b"ADDED", status=201)
    return  HttpResponseNotFound()

@login_required(login_url="authentication:login")
@csrf_exempt
def book_review(request):
    if request.method == 'POST':
        form = ReviewBookForm(request.POST)
        if form.is_valid():
            # Process the form data and save the review
            # Redirect to a success page or do something else
            form.save()
            return render(request)

    return render(request, 'book_review.html', {'form': form})


# Create your views here.
# import model products kesini, trs pake object.all()
# search pake ajax(url,view(cara aksesnya object.filter(name__contains=jajnjnasf),hbs itu render html))