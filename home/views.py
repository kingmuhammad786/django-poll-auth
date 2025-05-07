"""
Views for the Home application.

Defines the homepage view, rendering the index template.
Additional views can be added as the project expands.
"""

from django.shortcuts import render


def index(request):
    """Renders the homepage template."""
    return render(request, 'home/index.html')
