from django.shortcuts import render
from cart.cart import CartManager

# Create your views here.

def view_cart_items(request):
    cart = CartManager(request)
    context = {
        "cart": cart
    }
    return render(request, 'cart.html', context)