"""
Unit tests for the Polls application.

This file contains tests to validate the functionality of models
in the Polls app, ensuring correct behavior of question publishing
and voting mechanisms.
"""

from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question, Choice


class QuestionModelTests(TestCase):
    """Tests for the Question model."""

    def test_was_published_recently_with_future_question(self):
        """Ensure was_published_recently() returns False for future questions."""
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_date)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """Ensure was_published_recently() returns False for old questions."""
        old_date = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=old_date)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """Ensure was_published_recently() returns True for recent questions."""
        recent_date = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date=recent_date)
        self.assertIs(recent_question.was_published_recently(), True)


class ChoiceModelTests(TestCase):
    """Tests for the Choice model."""

    def setUp(self):
        """Set up test data before running tests."""
        self.question = Question.objects.create(
            question_text="Sample Question", pub_date=timezone.now()
        )
        self.choice = Choice.objects.create(
            question=self.question, choice_text="Sample Choice", votes=0
        )

    def test_choice_string_representation(self):
        """Verify the string representation returns the choice text."""
        self.assertEqual(str(self.choice), "Sample Choice")

    def test_vote_increment(self):
        """Ensure votes increase correctly."""
        self.choice.votes += 1
        self.choice.save()
        self.assertEqual(self.choice.votes, 1)

