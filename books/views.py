from django.shortcuts import render
from .models import Author, Category, Publisher, Product

# Create your views here.
def category_list(request):
    return {
        "categories": Category.objects.all()
    }

def book_list(request):
    books = Product.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books.html', context)