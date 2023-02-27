from django.contrib import admin
from .models import Author, Category, Publisher, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductFilter(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price']
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug_field': ('title', )}

admin.site.register(Author)
admin.site.register(Publisher)