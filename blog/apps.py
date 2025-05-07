"""
App configuration for the Blog application.

Defines settings for the Blog app, including the default auto field
used for model primary keys.
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configuration settings for the Blog app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

