from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10)
    cart = models.ManyToManyField(Katalog)
