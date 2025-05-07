"""
Models for the User Authentication application.

Defines data structures for managing user authentication and profiles.
"""

from django.db import models


class UserProfile(models.Model):
    """Example model for user profiles."""

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the username as the string representation of the model."""
        return self.username

