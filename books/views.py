from django.shortcuts import render
from .models import Author, Category, Publisher, BookName

# Create your views here.
def book_list(request):
    books = BookName.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books', context)