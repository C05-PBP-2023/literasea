from django.forms import ModelForm, TextInput
from .models import BookTracker

class addTrackerForm(ModelForm):
    class Meta:
        model = BookTracker
        fields = ['judul', 'halaman_terakhir']

        widgets = {
            'nama': TextInput(attrs={'class':'m-5'})
        }