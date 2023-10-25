from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user_ask = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ask")
    user_answer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_answer")
    question = models.TextField()
    answer = models.TextField()
