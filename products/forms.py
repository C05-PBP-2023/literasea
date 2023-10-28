from django import forms
from .models import Katalog

class BookFilterForm(forms.Form):
    author_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Author Name'}))
    publisher = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Publisher'}))
    published_year = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Year'}))

class AddBookForm(forms.Form):
   class Meta:
       model = Katalog
       fields = ['ISBN', 'Book_Title', 'Book_Author', 'Year_Of_Publication', 'Publisher', 'Image']