class ShoppingCart:
    products = {'iphone': 5, 'imac': 3, 'ipad': 2, 'iwatch': 4}
    prices = {'iphone': 800, 'imac': 4500, 'ipad': 5000, 'iwatch': 3000}

    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity, price):
        if name not in self.__class__products:
            raise Exception("invalid Product")
        elif quantity <= self.__class__products['name']:
            self.cart.append({'name': name, 'quantity': quantity, 'price': self.__class__prices['name']})
            self.__class__.products['name'] -= quantity
        else:
            raise ValueError("Product Out of stock")


    def total_cost(self):
        # total = sum([item['quantity']*item['price'] for item in self.cart])
        # return total     # we can use above list comprehension also IPO below logic
        total = 0
        for item in self.cart:
            total = total + item['quantity']*item['price']
        return total

    def remove_item(self, name):
        for item in self.cart:
            if item['name'] == name:
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                else:
                    self.cart.remove(item)


c1 = ShoppingCart()
c2 = ShoppingCart()
c3 = ShoppingCart()

c1.add_item("iphone", 2)
c2.add_item("imac", 1)
c1.remove_item("iphone")


