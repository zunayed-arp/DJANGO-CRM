from django.urls import path
from .views import *

app_name="books"

urlpatterns = [
    path('',BookListView.as_view(),name="home")
]