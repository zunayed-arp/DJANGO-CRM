from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    for x in latest_question_list:
        print(x.question_text)
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse(f"You're looking at Question {question_id}")

def results(request,question_id):
    response = f"You're looking at the results of {question_id}"
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"You're voting on question {question_id}")
