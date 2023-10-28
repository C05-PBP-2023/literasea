from django.forms import ModelForm, TextInput
from .models import History

class CheckoutForm(ModelForm):
    class Meta:
        model = History
        fields = ['nama', 'alamat']

        widgets = {
            'nama': TextInput(attrs={'class':'m-2 p-2 rounded-md h-[25px] w-[400px] border-[1px] border-[#00134E] border-opacity-30'}),
            'alamat': TextInput(attrs={'class':'m-2 p-2 rounded-md h-[25px] w-[400px] border-[1px] border-[#00134E] border-opacity-30'}),
        }