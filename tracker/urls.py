from django.urls import path
from .views import *

app_name = "tracker"

urlpatterns = [
    path("", show_tracked, name="show_tracked"),
    path("addtracked/", add_tracked, name="add_tracked"),
    path("addtracked/ajax/", add_tracked_ajax, name="add_tracked_ajax"),
]
