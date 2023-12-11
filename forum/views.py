from django.shortcuts import render
from products.models import Katalog
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forum.models import Question, Answer
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from forum.forms import *
import json


@login_required(login_url="authentication:login")
def show_main(request):
    questions = Question.objects.all().order_by("-id")
    context = {"questions": questions}
    return render(request, "qna.html", context)


@login_required(login_url="authentication:login")
def choose_book(request):
    books = Katalog.objects.all()
    form = QuestionForm(request.POST or None)

    context = {"products": books, "form": form}

    return render(request, "katalog_choose.html", context)


@csrf_exempt
def write_question(request):
    if request.method == "POST":
        title = request.POST.get("title")
        question = request.POST.get("question")
        user = request.user
        book_asked = Katalog.objects.get(pk=request.POST.get("id"))

        new_question = Question(
            user=user, book_asked=book_asked, title=title, question=question
        )
        new_question.save()

        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
def add_answer(request):
    if request.method == "POST":
        answer = request.POST.get("answer")
        question = Question.objects.get(pk=request.POST.get("id"))
        user = request.user

        new_answer = Answer(user=user, question=question, answer=answer)
        new_answer.save()

        question.answered = True
        question.save(update_fields=["answered"])

        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()


def get_answer_by_id(request, id):
    question = Question.objects.get(pk=id)
    answer = question.answer
    data = {"user": answer.user.userprofile.full_name, "answer": answer.answer}
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_questions(request):
    questions = Question.objects.all()
    data = []
    for question in questions:
        each_data = {
            "user_type": request.user.userprofile.user_type,
            "id": question.pk,
            "title": question.title,
            "question": question.question,
            "full_name": question.user.userprofile.full_name,
            "BookTitle": question.book_asked.BookTitle,
            "BookAuthor": question.book_asked.BookAuthor,
            "Image": question.book_asked.Image,
            "answered": question.answered,
        }
        if each_data["answered"]:
            each_data["answer"] = question.answer.answer
        data.append(each_data)

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_questions(request):
    questions = Question.objects.all()
    data = []
    for question in questions:
        each_data = {
            "user_type": request.user.userprofile.user_type,
            "id": question.pk,
            "title": question.title,
            "question": question.question,
            "full_name": question.user.userprofile.full_name,
            "BookTitle": question.book_asked.BookTitle,
            "BookAuthor": question.book_asked.BookAuthor,
            "Image": question.book_asked.Image,
            "answered": question.answered,
        }
        if each_data["answered"]:
            each_data["answer"] = question.answer.answer
            each_data["user_answer"] = question.answer.user.userprofile.full_name
        data.append(each_data)

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_questions_raw(request):
    questions = Question.objects.all()
    return HttpResponse(serializers.serialize("json", questions), content_type="application/json")


def get_answers_raw(request):
    answers = Answer.objects.all()
    return HttpResponse(serializers.serialize("json", answers), content_type="application/json")
