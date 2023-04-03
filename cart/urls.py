from django.urls import path
from .views import view_cart_items

app_name = 'cart'

urlpatterns = [
    path('', view_cart_items, name='view_cart_items'),
    # path('add/', )
#     path('add/', )
#     path('add/', )
]
