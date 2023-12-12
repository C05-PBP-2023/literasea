from django.urls import path
from authentication.views import *
from .views import *

app_name = 'cart'

urlpatterns = [
    path("", show_cart, name="show_cart"),
    path("checkout/", checkout_cart, name="checkout_cart"),
    path("history/", show_history, name="show_history"),
    path("owned/", show_owned, name="show_owned"),
    path("remove/<int:book_id>", remove_book_from_cart, name="remove"),
    path("get-history/", get_history_json, name="get_history_json"),

    path("get-cart/", get_cart_json, name='get_cart_json'),
    path("get-cart-id/<int:id>", get_cart_json_by_user_id, name="get_cart_json_by_user_id"),
    path("remove-book/<int:id>", remove_book_from_cart_ajax, name="remove_book_from_cart_ajax"),

    path("checkout-flutter/", checkout_cart_flutter, name="checkout_flutter"),
    path("remove-flutter/<int:user_id>/<int:book_id>", remove_book_from_cart_flutter, name="remove_flutter")
]
