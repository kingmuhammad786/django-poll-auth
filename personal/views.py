"""
Views for the Personal application.

Handles rendering pages such as Home, About, and Contact.
"""

from django.shortcuts import render


def root_view(request):
    """Renders the homepage template."""
    return render(request, 'personal/home.html')


def about_view(request):
    """Renders the About page template."""
    return render(request, 'personal/about.html')


def contact_view(request):
    """Renders the Contact page template."""
    return render(request, 'personal/contact.html')


def home_view(request):
    """Renders the Home page template."""
    return render(request, 'personal/home.html')

