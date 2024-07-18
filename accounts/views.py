from django.shortcuts import render, redirect

from .forms import UserUpdateForm
from .models import CustomUser


async def profile(request, username):
    """
    show user profile data
    """
    return render(request, "accounts/profile.html")


async def profile_edit(request):
    user = request.user

    if request.method == "GET":
        form = UserUpdateForm()

    else:
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile", user.username)

    context = {"form": form}
    return render(request, "accounts/profile-edit.html", context=context)
