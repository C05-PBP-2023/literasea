from django.urls import path
from authentication.views import *
from .views import *

app_name = 'cart'

urlpatterns = [
    path("", show_cart, name="show_cart"),
    path("checkout/", checkout_cart, name="checkout_cart"),
    path("history/", show_history, name="show_history"),
    path("owned/", show_owned, name="show_owned"),
]
