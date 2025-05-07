"""
Views for the User Authentication application.

Handles user registration, login, and profile display.
"""

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import RegistrationForm


def register(request: HttpRequest) -> HttpResponse:
    """Handles user registration.

    Args:
        request (HttpRequest): The request object containing user registration details.

    Returns:
        HttpResponse: The response rendering the user profile or registration page.
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save with commit=False to allow password hashing before final save.
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            return render(
                request,
                "authentication/user.html",
                {"username": user.username, "first_name": user.first_name},
            )
        else:
            # If the form is invalid, show the registration page again with error messages.
            return render(request, "authentication/register.html", {"form": form})
    else:
        form = RegistrationForm()
    return render(request, "authentication/register.html", {"form": form})


class CustomLoginView(LoginView):
    """Handles user login using Django's built-in authentication system."""
    template_name = "authentication/login.html"


def show_user(request: HttpRequest) -> HttpResponse:
    """Displays user profile details.

    Args:
        request (HttpRequest): The request object containing user session data.

    Returns:
        HttpResponse: The response rendering the user profile details page.
    """
    return render(
        request,
        "authentication/user.html",
        {"username": request.user.username, "first_name": request.user.first_name},
    )


# Expose login_view to be imported in the main URL configuration.
login_view = CustomLoginView.as_view()
