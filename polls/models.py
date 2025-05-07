"""
Models for the Polls application.

Defines the Question and Choice models, which store poll data.
"""

from django.db import models


class Question(models.Model):
    """Represents a poll question."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Returns the question text as the string representation."""
        return self.question_text


class Choice(models.Model):
    """Represents a possible answer for a poll question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Returns the choice text as the string representation."""
        return self.choice_text

