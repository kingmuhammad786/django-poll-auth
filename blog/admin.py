"""
Admin configuration for the Blog app.

Registers the Post model to the Django admin panel, allowing posts
to be managed through the admin interface.
"""

from django.contrib import admin
from .models import Post

# Register the Post model for admin management
admin.site.register(Post)

