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
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __len__(self):
        '''
        basket data and count item quantity
        '''
        return sum(item['qty'] for item in self.cart.values())

    def save(self):
        self.session.modified = True
