from django.shortcuts import render
from .models import Katalog

# Create your views here.
def show_main(request):

    context = {
        'products': Katalog.objects.all(),
    }

    return render(request, "main.html", context)