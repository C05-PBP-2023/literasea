from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', show_main, name='forum'),
    path('choose-book-review/', choose_book_review, name="choose_book_review"),
    path('add-review/', add_review, name="add_review"),
    path('add-review-flutter/', add_review, name="add_review_flutter"),
    path('choose-book-review-flutter/', add_review, name="choose_book_review_flutter"),
    path('json/', show_json, name="show_json"),
]