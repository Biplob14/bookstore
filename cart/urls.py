from django.urls import path
from .views import view_cart_items, add_to_cart

app_name = 'cart'

urlpatterns = [
    path('', view_cart_items, name='view_cart_items'),
    path('add/', add_to_cart, name='add_to_cart')
#     path('add/', )
#     path('add/', )
]
