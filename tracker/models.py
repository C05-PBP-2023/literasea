from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog


class BookTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    last_page = models.IntegerField()
    last_read_timestamp = models.DateTimeField(auto_now_add=True)
