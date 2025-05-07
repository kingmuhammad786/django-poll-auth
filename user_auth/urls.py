"""
URL configuration for User Authentication.

Defines routes for user registration, login, logout, and profile display.
"""

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("register/", views.register, name="register"),  # Handles user registration
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login"
    ),  # Custom login page using Django's built-in auth system
    path(
        "logout/",
        auth_views.LogoutView.as_view(http_method_names=["get", "post"], next_page="/"),
        name="logout"
    ),  # Allows both GET and POST methods for logout
    path("show_user/", views.show_user, name="show_user"),  # Displays user profile
]
