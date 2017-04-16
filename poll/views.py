from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Question


# using generic views
class IndexView(generic.ListView):
    # ListView uses by default the following template_name if not specified
    # in templates directory <app_name>/<model_name>_list.html
    template_name = 'poll/index.html'

    # the automatically generated context variable would be
    # <model_name>_list -> here specified and overwriten
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (Not including those 
        set to be published in the future)
        """
        # the filter says that it only returns those w/ the pub_date
        # less or equal to timezone.now() (earlier or now)
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question

    # DetailView uses by default the following template_name if not specified
    # in templates directory <app_name>/<model_name>_detail.html
    template_name = 'poll/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


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
