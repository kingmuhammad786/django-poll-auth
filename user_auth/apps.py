"""
App configuration for the User Authentication application.

Defines settings for the User Auth app, including the default auto field
used for model primary keys.
"""

from django.apps import AppConfig


class UserAuthConfig(AppConfig):
    """Configuration settings for the User Auth app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
