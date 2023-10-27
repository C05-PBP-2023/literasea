from django.forms import ModelForm
from .models import Review


class ReviewBookForm(ModelForm):
    class Meta:
        model = Review
        fields = ["user", "book_review",  "rating", "review_message"]