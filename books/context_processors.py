from .models import Category

def category_list(request):
    return {
        "categories": Category.objects.all().order_by('name')
    }