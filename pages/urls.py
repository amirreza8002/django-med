from django.urls import path

from .views import home, about, robots

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("robots.txt", robots, name="robots"),
]
