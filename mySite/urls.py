"""
URL configuration for MySite.

Defines the root routes for the project, linking different apps
such as home, personal, polls, blog, and user_auth.
"""

from django.contrib import admin
from django.urls import path, include
from user_auth.views import login_view  # Import the login view

urlpatterns = [
    path('', include('home.urls', namespace='home')),                   # Homepage routing (Home app)
    path('personal/', include('personal.urls', namespace='personal')),    # Personal app (About/Contact, etc.)
    path('polls/', include('polls.urls', namespace='polls')),             # Polls section
    path('blog/', include('blog.urls', namespace='blog')),                # Blog section
    path('user_auth/', include('user_auth.urls', namespace='user_auth')), # Authentication system
    path('login/', login_view, name='login'),                             # Direct mapping for custom login page
    path('admin/', admin.site.urls),                                      # Django admin panel
]
