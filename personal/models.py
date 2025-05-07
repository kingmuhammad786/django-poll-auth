"""
Models for the Personal application.

This file defines data structures for the Personal app, allowing content
to be stored and managed via Django’s ORM.
"""

from django.db import models


class PersonalModel(models.Model):
    """Example model for the Personal app."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the title as the string representation of the model."""
        return self.title

