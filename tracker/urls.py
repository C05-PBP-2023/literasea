from django.urls import path
from authentication.views import *
from .views import *

app_name = 'tracker'

urlpatterns = [
    path("", show_tracked, name="show_tracked"),
    path("addtracked/", add_tracked, name="add_tracked"),
]