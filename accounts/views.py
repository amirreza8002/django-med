from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .forms import UserUpdateForm


async def profile(request, username):
    """
    show user profile data
    """
    return render(request, "accounts/profile.html")


def profile_edit(request, username):
    user = get_user_model()
    instance = user.objects.get(username=username)

    if request.method == "GET":
        form = UserUpdateForm(
            initial={
                "first_name": instance.first_name,
                "last_name": instance.last_name,
                "birth": instance.birth,
                "phone_number": instance.phone_number,
            }
        )

    else:
        form = UserUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid:
            form.save()
            return redirect("profile", username=instance.username)

    context = {"form": form}
    return render(request, "accounts/profile-edit.html", context=context)
