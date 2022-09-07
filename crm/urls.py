
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('books.urls')),
    path('books-api/',include('apis.urls')),
    path('todos/',include('todos.urls')),
]
