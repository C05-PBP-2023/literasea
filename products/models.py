from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Katalog(models.Model):
    ISBN = models.CharField(_("ISBN"), max_length=20)
    BookTitle = models.CharField(_("Book-Title"), max_length=100)
    BookAuthor = models.CharField(_("Book-Author"), max_length=100)
    Publisher = models.CharField(_("Publisher"), max_length=100)
    Year_Of_Publication = models.IntegerField(_("Year-Of-Publication"))
    Image = models.ImageField(_("Image-URL-M"))