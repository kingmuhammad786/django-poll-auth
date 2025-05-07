"""
Unit tests for the Home application.

This file contains tests to validate the functionality of models in 
the Home app, ensuring that data is correctly stored and retrieved.
"""

from django.test import TestCase
from .models import HomeModel  # Replace with actual models when added


class HomeModelTest(TestCase):
    """Tests for the HomeModel."""

    def setUp(self):
        """Set up test data before running tests."""
        self.home_entry = HomeModel.objects.create(
            title="Welcome Message",
            description="This is the home page description."
        )

    def test_home_model_creation(self):
        """Ensure that a HomeModel instance is correctly stored."""
        entry = HomeModel.objects.get(title="Welcome Message")
        self.assertEqual(entry.description, "This is the home page description")

    def test_home_model_string_representation(self):
        """Verify the string representation returns the title."""
        self.assertEqual(str(self.home_entry), "Welcome Message")
