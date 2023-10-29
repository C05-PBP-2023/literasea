from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog


class BookTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    halaman_terakhir = models.IntegerField()
    tanggal = models.DateTimeField(auto_now_add=True)
