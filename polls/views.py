from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello now i'm at poll apps")
