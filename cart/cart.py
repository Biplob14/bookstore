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
            yield item

    def __len__(self):
        '''
        basket data and count item quantity
        '''
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        print("get total price")
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def get_item_total_price(self, product):
        if product in self.cart:

            print("product in cart: ", self.cart[product])

        return Decimal(self.cart[product]['price']) * Decimal(self.cart[product]['qty'])

    def delete(self, product):
        '''
        Delete item from cart session
        '''
        product_id = str(product)
        print('### session delete ###', product_id)
        if product_id in self.cart:
            print('deleting irem from cart')
            del self.cart[product_id]
            self.save()

    def update(self, product, prod_qty):
        '''
        update product on session
        '''
        product_id = str(product)
        # prod_qty = int(prod_qty)
        if product_id in self.cart:
            print("session item: ", self.cart)
            self.cart[product_id]['qty'] = int(prod_qty)
            self.save()

    def save(self):
        self.session.modified = True
