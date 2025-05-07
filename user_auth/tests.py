"""
Unit tests for the User Authentication application.

This file contains tests to validate user authentication and profile functionality.
"""

from django.test import TestCase
from .models import UserProfile  # Replace with actual models when added


class UserProfileTest(TestCase):
    """Tests for the UserProfile model."""

    def setUp(self):
        """Set up test data before running tests."""
        self.user = UserProfile.objects.create(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com"
        )

    def test_user_profile_creation(self):
        """Ensure a UserProfile instance is correctly stored."""
        user = UserProfile.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

    def test_user_profile_string_representation(self):
        """Verify the string representation returns the username."""
        self.assertEqual(str(self.user), "testuser")

