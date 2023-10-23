from .models import Category, Author


def category_list(request):
    return {
        "categories": Category.objects.all().order_by('name')
    }


def author_list(request):
    return {
        "authors": Author.objects.all().order_by('name').values('name')
    }
