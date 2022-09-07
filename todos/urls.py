from django.urls import path

from .views import *

urlpatterns = [
path('',ListTodo.as_view(),name="todo_list"),
path("<int:pk>/",DetailTodo.as_view(),name="todo_detail")
]