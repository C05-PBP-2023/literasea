from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    tanggal = models.DateField(auto_now_add=True)
    buku = models.ManyToManyField(Katalog)
