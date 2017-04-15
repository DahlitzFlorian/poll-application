from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # parentheses 'capture' the text of the url in it and send it
    # as argument to the method
    # ?P<question_id> ends up as question_id="" and the [0-9]+
    # stands for digits that have to stand there that it matches
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]