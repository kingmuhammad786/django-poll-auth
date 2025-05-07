"""
URL configuration for the Personal application.

Defines routes for various sections such as About, Contact, and Home.
Each route connects to its respective view function for rendering.
"""

from django.urls import path
from . import views

# Define namespace for URL referencing
app_name = 'personal'

urlpatterns = [
    path('', views.root_view, name='root'),  # Root route
    path('about/', views.about_view, name='about'),  # About page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('home/', views.home_view, name='home'),  # Home page
]

