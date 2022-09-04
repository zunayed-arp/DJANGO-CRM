from django.urls import path
from polls.views import *

urlpatterns = [
    path('index/',index,name='index')
]


