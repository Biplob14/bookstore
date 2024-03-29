from django.contrib import admin
from .models import Author, Category, Publisher, Product, Comment
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_field']
    prepopulated_fields = {'slug_field': ('name', )}


@admin.register(Product)
class ProductaAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price', 'is_active']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'author', 'is_active']
    prepopulated_fields = {'slug_field': ('title', )}


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_field']
    list_filter = ['name', 'slug_field']
    prepopulated_fields = {'slug_field': ('name', )}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass