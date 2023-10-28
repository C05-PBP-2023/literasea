from django.shortcuts import render, get_object_or_404, redirect
from .forms import addTrackerForm
from .models import BookTracker
from authentication.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse

def show_tracked(request):
    tracked = request.user.userprofile.tracked_books.all().order_by('-id')

    context = {
        "tracked": tracked,
    }

    return render(request, 'show_tracked.html', context)

def add_tracked(request):
    if request.method == 'POST':
        form = addTrackerForm(request.POST)
        judul = request.POST.get('judul')
        halaman_terakhir = request.POST.get('halaman_terakhir')
        
        if form.is_valid():
            new_tracker = form.save(commit=False)  
            new_tracker.user = request.user
            new_tracker.save() 

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.tracked_books.add(new_tracker)

            # Redirect to show_tracked page after form submission
            return HttpResponseRedirect(reverse('tracker:show_tracked'))
    else:
        form = addTrackerForm()

    owned = request.user.userprofile.owned_books.all()
    context = {'form': form, 'owned': owned}

    return render(request, "add_tracked.html", context)