from django.shortcuts import render, get_object_or_404, redirect
from .forms import addTrackerForm
from .models import BookTracker
from authentication.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from products.models import Katalog
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.contrib.auth.models import User


@login_required(login_url="authentication:login")
def get_tracked_books(request):
    tracked = request.user.userprofile.tracked_books.all().order_by(
        "-last_read_timestamp"
    )

    context = {
        "tracked": tracked,
    }

    return render(request, "show_tracked.html", context)


def get_tracked_books_flutter(request, user_id):
    tracked_books = BookTracker.objects.filter(user=user_id)
    if request.method == "GET":
        tracked_books_array = []
        for book in tracked_books:
            tracked_book = {
                "book_title": book.book_title,
                "last_page": book.last_page,
                "last_read_timestamp": book.last_read_timestamp,
            }
            tracked_books_array.append(tracked_book)
        return JsonResponse(
            {
                "status": "success",
                "message": "Successfully Retrieve Reading History!",
                "data": {"tracked_books": tracked_books_array},
            }
        )


@login_required(login_url="authentication:login")
@csrf_exempt
def add_tracked_books(request):
    if request.method == "POST":
        form = addTrackerForm(request.POST)
        book_id = request.POST.get("book")
        book = Katalog.objects.get(id=book_id)
        last_page = request.POST.get("last_page")
        current_time = timezone.now()

        # Cek apakah sudah ada tracker dengan book_title yang sama
        existing_tracker = BookTracker.objects.filter(
            book=book_id, user=request.user
        ).first()

        if existing_tracker:
            # Jika sudah ada, update last_page dan last_read_timestamp
            existing_tracker.last_page = last_page
            existing_tracker.last_read_timestamp = current_time
            existing_tracker.save()
        else:
            # Jika belum ada, buat objek baru
            new_tracker = form.save(commit=False)
            new_tracker.user = request.user
            new_tracker.last_read_timestamp = current_time
            new_tracker.book = book
            new_tracker.save()

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.tracked_books.add(new_tracker)

        # Redirect to show_tracked page after form submission
        return HttpResponseRedirect(reverse("tracker:show_tracked"))
    else:
        form = addTrackerForm()

    owned = request.user.userprofile.owned_books.all()
    context = {"form": form, "owned": owned}

    return render(request, "add_tracked.html", context)

@csrf_exempt
def add_tracked_books_flutter(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        book_id = request.POST.get("book")
        book = Katalog.objects.get(id=book_id)
        last_page = request.POST.get("last_page")
        current_time = timezone.now()

        # Cek apakah sudah ada tracker dengan book_title yang sama
        existing_tracker = BookTracker.objects.filter(
            book=book_id, user=user
        ).first()

        if existing_tracker:
            # Jika sudah ada, update last_page dan last_read_timestamp
            existing_tracker.last_page = last_page
            existing_tracker.last_read_timestamp = current_time
            existing_tracker.save()
            return JsonResponse(
                {"status": "success", "message": "Successfully Update Reading History!"}
            )
        else:
            # Jika belum ada, buat objek baru
            new_tracker = BookTracker(
                user=user,
                book=book,
                book_title=book.BookTitle,
                last_page=last_page,
                last_read_timestamp=current_time,
            )
            new_tracker.save()

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.tracked_books.add(new_tracker)

            return JsonResponse(
                {"status": "success", "message": "Successfully Add Reading History!"}
            )

    return JsonResponse({"status": "failed", "message": "Failed Add Reading History"})
