"""
URL configuration for the Blog application.

Defines routes for listing blog posts and viewing individual posts
using class-based views for cleaner, more efficient routing.
"""

from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Post

# Define namespace for URL referencing
app_name = 'blog'

urlpatterns = [
    # ListView: Displays all blog posts, sorted by most recent first
    path(
        '', 
        ListView.as_view(
            queryset=Post.objects.all().order_by('-date'), 
            template_name='blog.html'
        ), 
        name='index'
    ),
    
    # DetailView: Displays a single blog post based on its primary key (ID)
    path(
        '<int:pk>/', 
        DetailView.as_view(
            model=Post, 
            template_name='post.html'
        ), 
        name='detail'
    ),
]

