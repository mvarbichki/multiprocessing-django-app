from django.urls import path

from . import views

urlpatterns = [
    path("", views.parallel_processes, name="parallel_processes"),
]