from .models import Katalog
import django_filters

class KatalogFilter(django_filters.FilterSet):
    class Meta:
        model = Katalog
        fields = ['BookAuthor', 'Publisher', 'Year_Of_Publication']