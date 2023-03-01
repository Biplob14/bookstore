from django.urls import path
from .views import book_list, book_details

urlpatterns = [
    path('all/', book_list, name='all_books'),
    path('<slug:slug>/', book_details, name='book_details')
]
