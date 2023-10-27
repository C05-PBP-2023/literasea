from django.forms import ModelForm, TextInput
from .models import BookTracker

class TrackerForm(ModelForm):
    class Meta:
        model = BookTracker
        fields = ['nama_buku', 'halaman_terakhir']

        widgets = {
            'nama_buku': TextInput(attrs={'class':'m-5'})
        }