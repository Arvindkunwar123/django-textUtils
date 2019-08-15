from django.urls import path
from . import views

urlpatterns = [
    path("", views.Pipe.index, name="Home"),
    path("analyse/", views.Pipe().analyse, name="Home"),
    path("404", views.handler404, name="Home"),
    path(r"analyse/^$", views.handler404, name="Home"),
]


handler404 = 'utility.views.handler404'
