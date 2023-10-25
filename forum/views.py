from django.shortcuts import render
from authentication.models import UserProfile
from products.models import Katalog
from django.contrib.auth.decorators import login_required

@login_required(login_url="authentication:login")
def show_main(request):
    return render(request, 'qna.html', {})

@login_required(login_url="authentication:login")
def choose_book(request):
    books = Katalog.objects.all()

    context = {
        'products': books,
    }

    return render(request, "katalog_choose.html", context)

@login_required(login_url="authentication:login")
def write_question(request):
    pass