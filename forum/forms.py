from django.forms import ModelForm
from forum.models import *

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "question"]