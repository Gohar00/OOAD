from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_description(self):
        pass


class AudioProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_description(self):
        return "Audio"


class Clothing(Product):
    def __init__(self, name, price, count):
        super().__init__(name, price)
        self.count = count

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def get_description(self):
        return "Clothing"


class OrderOperations(ABC):

    @abstractmethod
    def total_price(self):
        pass


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.order_history = []

    @staticmethod
    def search(product_list, product_name=None, description=None, max_price=0):
        res = []
        for p in product_list:
            if product_name and product_name != p.get_name():
                continue
            if description and description != p.get_description():
                continue
            if max_price and max_price <= p.get_price():
                continue
            res.append(p.name)
        return f'Searched product: {res}'

    def purchase(self, product):
        self.order_history.append(product.name)
        if isinstance(product, Clothing):
            count = product.get_count()
            product.set_count(count - 1)

    def display_order_history(self):
        return f"{self.name}'s product history {self.order_history}"

    @staticmethod
    def leave_review(order):
        review = input(f'Enter your review for {order}')
        return review


class Order(OrderOperations):
    def __init__(self, customer, orders):
        self.customer = customer
        self.orders = orders
        self.price_total = 0

    def total_price(self):
        for order in self.orders:
            self.price_total += order.get_price()
        return f"Total price is {self.price_total}"


p1 = AudioProduct("Headphones", 50)
p2 = Clothing("T-shirt", 20, 10)


results = Customer.search([p1, p2], product_name="Headphones")
print(results)


c1 = Customer("Mary", "Mary@example.com")
c1.purchase(p1)
c1.purchase(p2)


print(c1.display_order_history())


o1 = Order(c1, [p1, p2])
print(p2.get_count())

print(o1.total_price())
