from django.urls import path
from main.views import show_main

app_name = 'products'

urlpatterns = [
    path('', show_main, name='show_main'),
]