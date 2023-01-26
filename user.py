import cart
from cart import *
from product import *

class User:

    def __init__(self, usname):
        self.usname = usname

    def Add_Cart(self, product):
        cart.add_product(product)
        return (f'Dear {self.usname} your product added in cart')

    def Remove_Item(self, product):
        cart.remove_product(product)
        ans = f'Dear {self.usname} your product removed of cart'
        return ans

    def Show_Item(self):
        return cart.show_products()

    def Reset(self):
        return cart.reset()

    def Buy_Products(self):
        total = cart.get_total_cost()
        print(f'Your purchase is worth {total} $')

    def Show_Products(self):
        return cart.show_products()



product1 = []
product1.append(Product("Phone",  800, "Samsung").get_name())
product1.append(Product("Phone",  800, "Samsung").get_price())
product1.append(Product("Phone",  800, "Samsung").get_description())

product2 = []
product2.append(Product("Teddy Bear", 100, "toy").get_name())
product2.append(Product("Teddy Bear", 100, "toy").get_price())
product2.append(Product("Teddy Bear", 100, "toy").get_description())

product3 = []
product3.append(Product("Python", 50, "book").get_name())
product3.append(Product("Python", 50, "book").get_price())
product3.append(Product("Python", 50, "book").get_description())

user1 = User('James')
user1.Add_Cart(product1)
user1.Add_Cart(product2)
user1.Add_Cart(product3)
user1.Show_Products()
user1.Buy_Products()












