from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Publisher, Product

# Create your views here.

def book_list(request):
    books = Product.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books.html', context)

def book_list_cat(request, bookCategory):
    books = Product.objects.filter(category__name=bookCategory)

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

def categorywise_list(request, slug):
    category_object = get_object_or_404(Category, slug=slug)
    books = Product.objects.filter(category=category_object, in_stock=True)

    context = {
        "books": books,
        "category": category_object
    }

    return context