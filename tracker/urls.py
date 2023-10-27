from django.urls import path
from .views import show_tracked, add_tracker

app_name = 'tracker'

urlpatterns = [
    path('', show_tracked, name='show_tracked'),
    path('add/', add_tracker, name='add_tracker'),
]