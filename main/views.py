from django.shortcuts import render
from products.models import Katalog

# Create your views here.
def show_main(request):
    # products = Katalog.objects.filter(user=request.user)

    context = {
        # 'name': request.user.username,
        'products': Katalog.objects.all(),
    }

    return render(request, "main.html", context)