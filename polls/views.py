from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from polls.models import Question, Choice
from django.template import loader
from django.urls import reverse

from django.views import generic
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """return the latest published questions"""
        return Question.objects.order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Question
    template_name: str = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name: str = "polls/results.html"


def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, pk=question_id)
    print("question", question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
