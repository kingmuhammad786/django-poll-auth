"""
Unit tests for the Blog application.

This file contains tests to validate the functionality of the Post model,
ensuring that blog posts are correctly stored and retrieved.
"""

from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):
    """Tests for the Post model."""

    def setUp(self):
        """Set up test data before running tests."""
        self.post = Post.objects.create(
            title="Test Post",
            body="This is a test blog post.",
            signature="Zohaib Muhammad"
        )

    def test_post_creation(self):
        """Ensure that a blog post is correctly stored in the database."""
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.body, "This is a test blog post")
        self.assertEqual(post.signature, "Zohaib Muhammad")

    def test_post_string_representation(self):
        """Verify the string representation of a post returns its title."""
        self.assertEqual(str(self.post), "Test Post")
