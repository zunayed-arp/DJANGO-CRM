from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *



class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer