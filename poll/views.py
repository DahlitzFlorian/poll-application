from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Question


# the default method which is calles if nothing else was
# specified by the url
def index(request):
    # fetches the latest questions ordered by the pub_date w/ limit 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # provides variables in the templates/context
    context = {'latest_question_list' : latest_question_list}

    return render(request, 'poll/index.html', context)


# view for details
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'poll/detail.html', {'question' : question})


# view results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'poll/results.html', {'question' : question})


# view vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'poll/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
