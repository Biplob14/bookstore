from .cart import CartManager


def cart(request):
    print('from cart context processor!!!!!!!!!!!!!')
    return {'basket': CartManager(request)}
