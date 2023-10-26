from django.shortcuts import render
from products.models import Katalog
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forum.models import Question
from django.http import HttpResponse, HttpResponseNotFound

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
@csrf_exempt
def write_question(request):
    if request.method == "POST":
        title = request.POST.get("title")
        question = request.POST.get("question")
        user = request.user
        book_reviewed = Katalog.objects.filter(pk=request.POST.get("id"))

        new_question = Question(user=user, book_reviewed=book_reviewed, title=title, question=question)
        new_question.save()

        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()

