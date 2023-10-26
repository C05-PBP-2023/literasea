from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_main, name='forum'),
    path('choose-book/', choose_book, name="choose_book"),
    path('add-question/', write_question, name="add_question/")
]