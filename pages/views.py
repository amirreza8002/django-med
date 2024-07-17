from django.shortcuts import render
from django.views.decorators.http import require_GET


async def home(request):
    return render(request, "pages/home.html")


@require_GET
async def about(request):
    return render(request, "pages/about.html")


@require_GET
async def robots(request):
    return render(request, "pages/robots.txt", content_type="text/plain")
