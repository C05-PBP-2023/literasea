from django.shortcuts import render, get_object_or_404, redirect
from .forms import addTrackerForm
from .models import BookTracker

from django.http import HttpResponseRedirect
from django.urls import reverse

from authentication.models import UserProfile

def show_tracked(request):
    tracked = request.user.userprofile.tracked_books.all().order_by('-id')

    context = {
        "tracked": tracked,
    }

    return render(request, 'show_tracked.html', context)

def add_tracked(request):
    if request.method == 'POST':
        form = addTrackerForm(request.POST)
        if form.is_valid():
            new_tracker = form.save(commit=False)  
            new_tracker.user = request.user
            new_tracker.save() 
            
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.tracked_books.add(new_tracker)

            # owned = request.user.userprofile.owned_books.all()
            # context = {'form': form, 'owned': owned}

            # return render(request, "add_tracked.html", context)
            return HttpResponseRedirect(reverse('tracker:show_tracked'))

    else:
        form = addTrackerForm()

    owned = request.user.userprofile.owned_books.all()
    context = {'form': form, 'owned': owned}

    return render(request, "add_tracked.html", context)