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
