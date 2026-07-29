from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def ui(request):
    return render(request, "pages/ui.html")


def robots_txt(request):
    return HttpResponse(
        render(request, "robots.txt").content,
        content_type="text/plain",
    )

def health(request):
    return JsonResponse(
        {
            "status": "ok",
            "application": "Bachkatov Portfolio",
        }
    )