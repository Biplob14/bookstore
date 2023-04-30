from .cart import CartManager


def cart(request):
    return {'basket': CartManager(request)}
