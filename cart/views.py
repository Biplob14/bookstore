from django.shortcuts import render

# Create your views here.

def view_cart_items(request):
    return render(request, 'cart.html')