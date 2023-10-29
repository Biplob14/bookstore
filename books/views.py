from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Product, Comment
from django.db.models import Q

# Create your views here.


def book_list(request):
    # query with custom model manager product
    search_post = request.GET.get('search')
    if search_post:
        books = Product.products_available.filter(
            Q(author__name__icontains=search_post) |
            Q(title__icontains=search_post) |
            Q(category__name__icontains=search_post) |
            Q(publisher__name__icontains=search_post) |
            Q(description__icontains=search_post)
        )
    else:
        books = Product.products_available.all()

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
    comments = Comment.objects.filter(product=book)
    print("book: ", comments)
    for comment in comments:
        print(comment.body)
    
    context = {
        "book": book,
        "comments": comments
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


def book_search(request):
    pass
