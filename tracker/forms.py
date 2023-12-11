from django import forms
from django.forms import ModelForm
from tracker.models import BookTracker


class addTrackerForm(ModelForm):
    class Meta:
        model = BookTracker
        fields = ["judul", "halaman_terakhir"]

        widgets = {
            "judul": forms.Select(attrs={"class": "w-full p-2 border rounded"}),
            "halaman_terakhir": forms.NumberInput(
                attrs={"class": "w-full p-2 border rounded"}
            ),
        }


"""
   - addTrackerForm:
     - formulir untuk menambahkan entri buku ke dalam BookTracker
     - Memanfaatkan model BookTracker
     - Menyertakan widget khusus untuk `judul` (berupa dropdown/select) dan `halaman_terakhir` (berupa input angka). asumsikan judul buku unique :D

"""
