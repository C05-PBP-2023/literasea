from django.urls import path
from .views import *

app_name = "tracker"

urlpatterns = [
    path("", show_tracked, name="show_tracked"),
    path("addtracked/", add_tracked, name="add_tracked"),
    path("addtracked/ajax/", add_tracked_ajax, name="add_tracked_ajax"),
]

"""
   - `show_tracked`: Menampilkan daftar buku yang telah dilacak.
   - `add_tracked`: Menampilkan formulir untuk menambahkan buku yang akan dilacak.
   - `add_tracked_ajax`: Endpoint untuk menangani permintaan AJAX dari formulir tambah buku.

"""
