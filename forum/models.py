from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_asked = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    question = models.TextField()
    

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.TextField()
