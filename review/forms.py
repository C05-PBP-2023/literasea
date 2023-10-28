from django.forms import ModelForm
from .models import Review

class ReviewBookForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review_message"]