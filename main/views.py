from django.shortcuts import render

def show_main(request):
    context = {"user": request.user}
    return render(request, "main.html", context)
