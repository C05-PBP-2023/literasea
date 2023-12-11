from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', show_main, name='forum'),
    path('choose-book-review/', choose_book_review, name="choose_book_review"),
    path('add-review/', add_review, name="add_review"),
    path('add-review-flutter/', add_review_flutter, name="add_review_flutter"),
    path('get-book-review/', get_book_review, name="get_book_review"),
    path('get-book-review/<int:id>', get_book_review_by_id, name="get_book_review_by_id"),
    path('json/', show_json, name="show_json"),
    path('show-review-flutter/', show_review_flutter, name="show_review_flutter"),
    path('get-latest-reviews/', get_latest_reviews, name="get_latest_reviews"),
]