from django.shortcuts import render
from cart.cart import CartManager
from django.shortcuts import get_object_or_404
from books.models import Product
from django.http import JsonResponse

# Create your views here.


def view_cart_items(request):
    context = {"cart": CartManager(request)}

    return render(request, 'cart.html', context)


def add_to_cart(request):
    cart = CartManager(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product_obj = get_object_or_404(Product, id=product_id)
        cart.add(product=product_obj, qty=product_qty)
        print("on add to cart.........................", product_obj)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        print("####################", response)
        return response

def cart_item_del(request):
    cart = CartManager(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        # invoke delete method from cart
        cart.delete(product=product_id)
        response = JsonResponse({
            'success': True
        })
        return response
