"""
URL configuration for the Polls application.

Defines routes for listing polls, viewing details, voting, and viewing results.
Additionally, includes a route for viewing blog posts by year.
"""

from django.urls import path
from . import views

# Define namespace for URL referencing
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),  # Lists questions on the index page
    path('<int:question_id>/', views.detail, name='detail'),  # Poll details
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Voting logic
    path('<int:question_id>/results/', views.results, name='results'),  # Poll results
    path('blog/<int:year>/', views.blog_detail, name='blog_detail'),  # Blog posts by year
]

