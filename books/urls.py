from django.urls import path
from .views import book_list, book_details, author_books

app_name = 'books'

urlpatterns = [
    path('all/', book_list, name='all_books'),
    path('<slug:slug>/', book_details, name='book_details'),
    path('author/<slug:slug>/', author_books, name='author_books'),
]
