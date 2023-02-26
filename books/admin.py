from django.contrib import admin
from .models import Author, Category, Publisher, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Product)