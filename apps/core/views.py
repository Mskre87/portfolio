from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def ui(request):
    return render(request, "pages/ui.html")