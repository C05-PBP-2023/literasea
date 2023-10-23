from django.urls import path
from products.views import show_katalog, book_detail

app_name = 'products'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('book_detail/<int:book_id>/', book_detail, name='book_detail')

]