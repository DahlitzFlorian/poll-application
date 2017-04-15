from django.shortcuts import render
from django.http import HttpResponse


# the default method which is calles if nothing else was
# specified by the url
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# view for details
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# view results
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# view vote
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
