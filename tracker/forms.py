from django import forms
from django.forms import ModelForm
from tracker.models import BookTracker


class addTrackerForm(ModelForm):
    class Meta:
        model = BookTracker
        fields = ["book_title", "last_page"]

        widgets = {
            "book_title": forms.Select(attrs={"class": "w-full p-2 border rounded"}),
            "last_page": forms.NumberInput(
                attrs={"class": "w-full p-2 border rounded"}
            ),
        }
