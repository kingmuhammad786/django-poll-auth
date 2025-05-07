"""
App configuration for the Home application.

Defines settings for the Home app, including the default auto field
used for model primary keys.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Configuration settings for the Home app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
