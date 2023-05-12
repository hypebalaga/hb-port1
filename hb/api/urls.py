from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.allblog, name="blog"),
    path("blog/<int:id>", views.blog, name="blog"),
]
