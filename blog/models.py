"""
Models for the Blog application.

Defines the Post model, which represents blog posts in the database.
Each post includes a title, body content, author signature, and a timestamp.
"""

from django.db import models


class Post(models.Model):
    """Represents a blog post with title, content, author, and timestamp."""
    
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Zohaib Muhammad")
    date = models.DateTimeField(auto_now_add=True)  # Sets date when post is created

    def __str__(self):
        """Returns the title as the string representation of a post."""
        return self.title

