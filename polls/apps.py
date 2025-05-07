"""
App configuration for the Polls application.

Defines settings for the Polls app, including the default auto field
used for model primary keys.
"""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """Configuration settings for the Polls app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

