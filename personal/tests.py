"""
Unit tests for the Personal application.

This file contains tests to validate the functionality of models in 
the Personal app, ensuring data is correctly stored and retrieved.
"""

from django.test import TestCase
from .models import PersonalModel  # Replace with actual models when added


class PersonalModelTest(TestCase):
    """Tests for the PersonalModel."""

    def setUp(self):
        """Set up test data before running tests."""
        self.personal_entry = PersonalModel.objects.create(
            title="Test Entry",
            description="This is a test description."
        )

    def test_personal_model_creation(self):
        """Ensure a PersonalModel instance is correctly stored."""
        entry = PersonalModel.objects.get(title="Test Entry")
        self.assertEqual(entry.description, "This is a test description")

    def test_personal_model_string_representation(self):
        """Verify the string representation returns the title."""
        self.assertEqual(str(self.personal_entry), "Test Entry")

