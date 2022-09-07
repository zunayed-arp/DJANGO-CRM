from django.shortcuts import render

from django.views import generic
from .models import Book



class BookListView(generic.ListView):
    model = Book
    template_name: str = "books/book_list.html"
    
