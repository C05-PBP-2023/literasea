from django.shortcuts import render, get_object_or_404, redirect
from .forms import addTrackerForm
from .models import BookTracker
from authentication.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone  # Import timezone

def show_tracked(request):
    tracked = request.user.userprofile.tracked_books.all().order_by('-tanggal')  # Mengurutkan berdasarkan tanggal, dari terbaru ke terlama

    context = {
        "tracked": tracked,
    }

    return render(request, 'show_tracked.html', context)

def add_tracked(request):
    if request.method == 'POST':
        form = addTrackerForm(request.POST)
        judul = request.POST.get('judul')
        halaman_terakhir = request.POST.get('halaman_terakhir')
        current_time = timezone.now()

        # Cek apakah sudah ada tracker dengan judul yang sama
        existing_tracker = BookTracker.objects.filter(judul=judul, user=request.user).first()

        if existing_tracker:
            # Jika sudah ada, update halaman_terakhir dan tanggal
            existing_tracker.halaman_terakhir = halaman_terakhir
            existing_tracker.tanggal = current_time
            existing_tracker.save()
        else:
            # Jika belum ada, buat objek baru
            new_tracker = form.save(commit=False)  
            new_tracker.user = request.user
            new_tracker.tanggal = current_time
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

def add_tracked_ajax(request):
    if request.method == 'POST':
        form = addTrackerForm(request.POST)
        judul = request.POST.get('judul')
        halaman_terakhir = request.POST.get('halaman_terakhir')
        current_time = timezone.now()

        existing_tracker = BookTracker.objects.filter(judul=judul, user=request.user).first()

        if existing_tracker:
            existing_tracker.halaman_terakhir = halaman_terakhir
            existing_tracker.tanggal = current_time
            existing_tracker.save()
        else:
            new_tracker = form.save(commit=False)  
            new_tracker.user = request.user
            new_tracker.tanggal = current_time
            new_tracker.save() 

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.tracked_books.add(new_tracker)

        return JsonResponse({'status': 'success', 'message': 'Tracker updated successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})