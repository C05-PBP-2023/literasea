from django.db import models
from django.contrib.auth.models import User

class BookTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    halaman_terakhir = models.IntegerField()
    tanggal = models.DateField(auto_now_add=True)