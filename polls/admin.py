"""
Admin configuration for the Polls application.

Registers models to enable management via Django's admin panel.
"""

from django.contrib import admin
from .models import Question, Choice

# Register models for admin management
admin.site.register([Question, Choice])
