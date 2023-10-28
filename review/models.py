from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog
from django.core.validators import MaxValueValidator, MinValueValidator 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_review = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=((i,i) for i in range(1, 6)))
    review_message = models.TextField()


# Create your models here.
