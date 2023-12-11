from django.urls import path
from .views import *

app_name = "tracker"

urlpatterns = [
    path("", show_tracked, name="show_tracked"),
    path("addtracked/", add_tracked, name="add_tracked"),  # Tanpa AJAX
    path("addtracked/ajax/", add_tracked_ajax, name="add_tracked_ajax"),  # Dengan AJAX
    path("tracked-books/mobile/<int:user_id>", get_tracked_books_flutter, name="get_tracked_books"),
]
