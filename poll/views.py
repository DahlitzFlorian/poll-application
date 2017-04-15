from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render

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
    # first possible solution
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    # more shorten w/ making use of importing from django.shortcuts
    # get_object_or_404:
    # question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'poll/detail.html', {'question' : question})


# view results
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# view vote
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
