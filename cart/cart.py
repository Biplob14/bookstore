from books.models import Product
from decimal import Decimal

class CartManager():
    ''' handle cart session '''

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')

        if 'skey' not in self.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] += qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.save()

    def __iter__(self):
        """ return cart item from session with product_id """
        product_ids = self.cart.keys()
        products = Product.products_available.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']

        print("iter: ", cart.values())
        yield item

    def __len__(self):
        '''
        basket data and count item quantity
        '''
        return sum(item['qty'] for item in self.cart.values())

    def save(self):
        self.session.modified = True
