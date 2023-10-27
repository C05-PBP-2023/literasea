from django.forms import ModelForm, TextInput
from .models import History

class CheckoutForm(ModelForm):
    class Meta:
        model = History
        fields = ['nama', 'alamat']

        widgets = {
            'nama': TextInput(attrs={'class':'m-5'})
        }