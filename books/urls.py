from django.urls import path
from .views import book_list

urlpatterns = [
    path('all/', book_list, name='all_books')
]
