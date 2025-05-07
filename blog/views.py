"""
Views for the Blog application.

Defines class-based views for listing blog posts and viewing individual posts.
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """Displays a list of blog posts, ordered by most recent."""

    model = Post
    template_name = "blog/blog.html"

    def get_queryset(self):
        """Returns the latest 25 blog posts, ordered by date."""
        return Post.objects.all().order_by('-date')[:25]


class BlogDetailView(DetailView):
    """Displays the details of a single blog post."""

    model = Post
    template_name = "blog/post.html"

