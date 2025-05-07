"""
Views for the Polls application.

Handles poll listings, voting, result display, and blog post retrieval.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice


def index(request):
    """Displays the latest poll questions.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered page with latest poll questions.
    """
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


def detail(request, question_id):
    """Displays details of a specific poll question.

    Args:
        request (HttpRequest): The request object.
        question_id (int): The ID of the poll question.

    Returns:
        HttpResponse: Rendered page displaying poll details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required(login_url='/login/')
def vote(request, question_id):
    """Handles voting logic for a poll question.

    Restricts voting access to logged-in users.

    Args:
        request (HttpRequest): The request object.
        question_id (int): The ID of the poll question.

    Returns:
        HttpResponseRedirect: Redirects to the results page after voting.
        HttpResponse: Renders poll detail page in case of errors.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    """Displays results of a specific poll question.

    Args:
        request (HttpRequest): The request object.
        question_id (int): The ID of the poll question.

    Returns:
        HttpResponse: Rendered page displaying poll results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def blog_detail(request, year):
    """Handles blog posts retrieval based on the given year.

    Args:
        request (HttpRequest): The request object.
        year (int): The year for filtering blog posts.

    Returns:
        HttpResponse: Message indicating blog posts from the specified year.
    """
    return HttpResponse(f"You're looking at blog posts from the year {year}.")
