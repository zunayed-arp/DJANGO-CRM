from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        'latest_question_list':latest_question_list
    }
    # output = ','.join([q.question_text for q in latest_question_list])
    
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    return HttpResponse(f"You're looking at Question {question_id}")

def results(request,question_id):
    response = f"You're looking at the results of {question_id}"
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"You're voting on question {question_id}")
