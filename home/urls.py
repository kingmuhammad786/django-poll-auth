"""
URL configuration for the Home application.

Defines routing for the homepage, linking it to the `index` view.
"""

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
]
