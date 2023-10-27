from django.urls import path
from review.views import show_review, pilih_buku, review_book

app_name = 'review'

urlpatterns = [
    path('',show_review, name='show_review'),
    path('pilih-buku/', pilih_buku, name='pilih_buku'),
    path('review-book/', review_book, name='review_book')
]