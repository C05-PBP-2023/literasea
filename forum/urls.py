from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_main, name='forum'),
    path('choose-book/', choose_book, name="choose_book"),
    path('add-question/', write_question, name="add_question"),
    path('add-answer/', add_answer, name="add_answer"),
    path('get-answer/<int:id>', get_answer_by_id, name="get_answer")
]