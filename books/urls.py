from django.urls import path
from .views import book_list, book_details, author_books, book_list_cat

app_name = 'books'

urlpatterns = [
    path('all/', book_list, name='all_books'),
    path('category/<str:bookCategory>/', book_list_cat, name='categorise_books'),
    path('<slug:slug>/', book_details, name='book_details'),
    path('author/<slug:slug>/', author_books, name='author_books'),
    path('category/<slug:slug>/', author_books, name='category_books'),
]
