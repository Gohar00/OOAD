class ShoppingCart:

    def __init__(self):
        self._products = []

    def add_product(self, item):
        self._products.append(item)

    def remove_product(self, item):
        self._products.remove(item)

    def get_total_cost(self):
        total = 0
        for item in self._products:
            total = total + item[1]
        return total

    def show_products(self):
        for item in self._products:
            print(item)

    def reset(self):
        self._products = []

cart = ShoppingCart()





