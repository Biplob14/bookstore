from django.shortcuts import render, get_object_or_404
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

def book_details(request, slug):
    book = get_object_or_404(Product, slug_field=slug, in_stock=True)
    context = {
        "book": book
    }
    return render(request, 'book_details.html', context)

def author_books(request, slug):
    author_object = get_object_or_404(Author, slug_field=slug)
    books = Product.objects.filter(author=author_object, in_stock=True)
    
    context = {
        "books": books,
        "author": author_object
    }
    return render(request, 'author.html', context)