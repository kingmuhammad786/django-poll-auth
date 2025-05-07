"""
App configuration for the Personal application.

Defines settings for the Personal app, including the default auto field
used for model primary keys.
"""

from django.apps import AppConfig


class PersonalConfig(AppConfig):
    """Configuration settings for the Personal app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'
