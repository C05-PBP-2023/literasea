from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_main, name='forum'),
    path('choose-book/', choose_book, name="choose_book"),
    path('add-question/', write_question, name="add_question"),
    path('add-question-mobile/', write_question_mobile,
         name="add_question_mobile"),
    path('add-answer/', add_answer, name="add_answer"),
    path('get-answer/<int:id>', get_answer_by_id, name="get_answer"),
    path('get-questions/', get_questions, name="get_questions"),
    path('get-questions-mobile/', get_questions_mobile,
         name="get_questions_mobile"),
    path('add-answer-mobile/', add_answer_mobile, name="add_answer_mobile"),
]
