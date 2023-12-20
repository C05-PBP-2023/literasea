from django.shortcuts import render, reverse, get_object_or_404
from .forms import addTrackerForm
from .models import BookTracker
from authentication.models import UserProfile
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from products.models import Katalog
from django.contrib.auth.models import User
import json


@login_required(login_url="authentication:login")
def show_tracked_books(request):
    tracked = request.user.userprofile.tracked_books.all().order_by(
        "-last_read_timestamp"
    )
    context = {"tracked": tracked}
    return render(request, "show_tracked_books.html", context)


def get_tracked_books_flutter(request, user_id):
    tracked_books = BookTracker.objects.filter(user=user_id).values(
        "book_title", "last_page", "last_read_timestamp"
    )
    tracked_books_array = list(tracked_books)
    retrieved_books_array = []
    for t in tracked_books_array:
        book = Katalog.objects.filter(BookTitle=t["book_title"]).first()
        info = {
            "book_image": book.Image,
            "book_title": t["book_title"],
            "last_page": t["last_page"],
            "last_read_timestamp": t["last_read_timestamp"],
        }
        retrieved_books_array.append(info)
    return JsonResponse(
        {
            "status": "success",
            "message": "Successfully Retrieve Reading History!",
            "data": {"tracked_books": retrieved_books_array},
        }
    )


@login_required(login_url="authentication:login")
@csrf_exempt
def add_tracked_books(request):
    if request.method == "POST":
        book_id = request.POST.get("book")
        book = get_object_or_404(Katalog, id=book_id)
        form_data = {
            "book_title": book.BookTitle,
            "last_page": request.POST.get("last_page"),
        }
        form = addTrackerForm(form_data)

        if form.is_valid():
            last_page = form.cleaned_data["last_page"]
            current_time = timezone.now()

            existing_tracker = BookTracker.objects.filter(
                book=book_id, user=request.user
            ).first()

            if existing_tracker:
                existing_tracker.last_page = last_page
                existing_tracker.last_read_timestamp = current_time
                existing_tracker.save()
            else:
                new_tracker = form.save(commit=False)
                new_tracker.user = request.user
                new_tracker.last_read_timestamp = current_time
                new_tracker.book = book
                new_tracker.save()

                user_profile, created = UserProfile.objects.get_or_create(
                    user=request.user
                )
                user_profile.tracked_books.add(new_tracker)

            return HttpResponseRedirect(reverse("tracker:show_tracked_books"))
        else:
            # Return JsonResponse with form errors
            return JsonResponse({"status": "failed", "errors": form.errors})

    else:
        form = addTrackerForm()

    owned = request.user.userprofile.owned_books.all()
    context = {"form": form, "owned": owned}
    return render(request, "add_tracked_books.html", context)


@csrf_exempt
def add_tracked_books_flutter(request, user_id):
    if request.method == "POST":
        tracked_book = json.loads(request.body)
        last_page = tracked_book["last_page"]
        current_time = timezone.now()
        book_id = tracked_book["book"]

        existing_tracked_book = BookTracker.objects.filter(
            book=book_id, user=user_id
        ).first()

        if existing_tracked_book:
            existing_tracked_book.last_page = last_page
            existing_tracked_book.last_read_timestamp = current_time
            existing_tracked_book.save()
            return JsonResponse(
                {"status": "success", "message": "Successfully Update Reading History!"}
            )
        else:
            new_tracked_book = BookTracker(
                user=User.objects.get(id=user_id),
                book=Katalog.objects.get(id=book_id),
                book_title=Katalog.objects.get(id=book_id).title,
                last_page=last_page,
                last_read_timestamp=current_time,
            )
            new_tracked_book.save()

            return JsonResponse(
                {"status": "success", "message": "Successfully Add Reading History!"}
            )

    return JsonResponse({"status": "failed", "message": "Failed Add Reading History"})


@csrf_exempt
def get_books_flutter(request):
    if request.method == "GET":
        books = Katalog.objects.all()
        return JsonResponse({"books": books})
    return JsonResponse({"error": "Invalid request method"}, status=400)
