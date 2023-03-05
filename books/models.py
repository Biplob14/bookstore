from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/author/', blank=True)
    slug_field = models.SlugField(max_length=256, blank=True)
    bio = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("books:author_books", args=[self.slug_field])

    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'    

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='images/product', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    slug_field = models.SlugField(max_length=256, unique=True)
    rating = models.IntegerField(default=0, validators = [MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('books:book_details', args=[self.slug_field])


    def __str__(self):
        return self.title