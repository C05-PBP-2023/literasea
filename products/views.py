from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'products': products,
    }

    return render(request, "main.html", context)