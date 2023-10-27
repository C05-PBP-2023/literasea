from django.db import models
from django.contrib.auth.models import User
from products.models import Katalog

class BookTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_buku = models.CharField(max_length=255)
    halaman_terakhir = models.PositiveIntegerField()
    tanggal = models.DateField(auto_now_add=True)
    # buku = models.ManyToManyField(Katalog)