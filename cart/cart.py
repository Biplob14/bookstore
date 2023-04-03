from books.models import Product
from decimal import Decimal


class CartManager():
    ''' handle cart session '''

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('key')

        if 'skey' not in self.session:
            cart = self.session['skey'] = {}
        self.cart = cart
