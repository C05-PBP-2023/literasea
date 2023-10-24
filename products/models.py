from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Katalog(models.Model):
    id = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=13)
    BookTitle = models.CharField(max_length=255)
    BookAuthor = models.CharField(max_length=255)
    Year_Of_Publication = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=255)
    Image = models.URLField()