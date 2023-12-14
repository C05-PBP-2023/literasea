from django.urls import path
from products.views import show_katalog, book_detail, add_book, get_book, get_book_by_id, add_book, add_to_cart, fungsi_haram

app_name = 'products'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('book_detail/<int:book_id>/', book_detail, name='book_detail'),
    path('add_book/<int:book_id>/<int:user_id>/', add_book, name='add_book'),
    path('get_book/', get_book, name='get_book'),
    path('get_book/<int:id>/', get_book_by_id, name="get_book_by_id"),
    path('add_book/', add_book, name='add_book'),
    path('add_to_cart/<int:book_id>/<int:user_id>/', add_to_cart, name='add_to_cart')
]