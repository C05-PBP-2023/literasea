from django.urls import path
from .views import *

app_name = "tracker"

urlpatterns = [
    path("", show_tracked_books, name="show_tracked_books"),  # Default
    path(
        "mobile/<int:user_id>",
        get_tracked_books_flutter,
        name="get_tracked_books_flutter",
    ),  # AJAX
    path("add/", add_tracked_books, name="add_tracked_books"),  # Default
    path(
        "add/mobile/<int:user_id>",
        add_tracked_books_flutter,
        name="add_tracked_books_flutter",
    ),  # AJAX
]
