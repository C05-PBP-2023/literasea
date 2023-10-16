from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.charField(max_length=100)
    email = models.emailField(max_length=100)
    user_type = models.charField(max_length=10)
