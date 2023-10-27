from django.shortcuts import render, get_object_or_404
from .forms import TrackerForm
from .models import BookTracker
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from authentication.models import UserProfile

@login_required(login_url="authentication:login")
def show_tracked(request):
    tracker = request.user.userprofile.tracker.all()

    context = {
        "tracker": tracker,
    }

    return render(request, 'book_tracker.html', context)

@csrf_exempt
def add_tracker(request):
    form = TrackerForm(request.POST or None)
    owned = request.user.userprofile.owned_books.all()

    context = {
        "owned": owned,
    }
    
    if form.is_valid() and request.method == 'POST':
        book_tracker = form.save(commit=False)
        book_tracker.user = request.user
        
        form.save()

        for book in request.user.userprofile.tracker.all():
            request.user.userprofile.tracker.add(book)

        return HttpResponseRedirect(reverse('tracker:show_tracked'))
    
    return render(request, "add_tracker.html", {"form": form}, context)