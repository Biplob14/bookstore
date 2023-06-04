from django.urls import path
from .views import view_cart_items, add_to_cart, cart_item_del

app_name = 'cart'

urlpatterns = [
    path('', view_cart_items, name='view_cart_items'),
    path('delete/', cart_item_del, name='delete_cart_items'),
    path('add/', add_to_cart, name='add_to_cart')
]
