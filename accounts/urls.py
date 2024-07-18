from django.urls import path, include

from .views import profile_edit, profile


urlpatterns = (
    path("<str:username>/profile/", profile, name="profile"),
    path("<str:username>/profile/edit/", profile_edit, name="profile-edit"),
    path("", include("allauth.urls")),
)
