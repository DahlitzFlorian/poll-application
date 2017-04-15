from django.shortcuts import render
from django.http import HttpResponse


# the default method which is calles if nothing else was
# specified by the url
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
