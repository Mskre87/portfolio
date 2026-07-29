from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ui/", views.ui, name="ui"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("health/", views.health, name="health"),
]