from django.conf.urls import url
from . import views


# specify an url namespace
app_name = 'poll'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # parentheses 'capture' the text of the url in it and send it
    # as argument to the method
    # ?P<question_id> ends up as question_id="" and the [0-9]+
    # stands for digits that have to stand there that it matches

    # the 'name' value is called by the {% url %} template tag

    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]