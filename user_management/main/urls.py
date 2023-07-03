from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.signup, name="sign-up"),
    path("create-post", views.create_post, name="create-post"),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
]
