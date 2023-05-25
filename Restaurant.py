from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    def add_dish(self, dish, price):
        pass

    @abstractmethod
    def remove_dish(self, dish):
        pass

    @abstractmethod
    def view_menu(self):
        pass


class Appetizers(Menu):

    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish, price):
        self.dishes[dish] = price

    def remove_dish(self, dish):
        if dish in self.dishes:
            del self.dishes[dish]

    def view_menu(self):
        print("Appettizers menu: ")
        for dish, price in self.dishes.items():
            print(f'{dish}: {price}')

class Entrees(Menu):

    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish, price):
        self.dishes[dish] = price

    def remove_dish(self, dish):
        if dish in self.dishes:
            del self.dishes[dish]

    def view_menu(self):
        print("Entrees menu: ")
        for dish, price in self.dishes.items():
            print(f'{dish} - {price}')


class Orders:
    def __init__(self, customer, dishes, total_price):
        self.customer = customer
        self.dishes = dishes
        self.total_price = total_price

    def __str__(self):
        return f"Customer: {self.customer}\nDishes: {self.dishes}\nTotal_price: {self.total_price} "


class Customers:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.orders = []

    def view_menu(self, menu):
        menu.view_menu()

    def place_order(self, menu):
        dishes = {}
        total_price = 0
        while True:
            dish = input("Enter the name of the dish to order or press 'q' to finish: ")
            if dish == 'q':
                break
            if dish in menu.dishes:
                price = menu.dishes[dish]
                dishes[dish] = price
                total_price += price
                print(f"{dish} added to the order.")
            else:
                print(f'{dish} is not available on the menu')
        if dishes:
            order = Orders(self.name, dishes, total_price)
            self.orders.append(order)
        else:
            print("No dishes were added to the order.")

    def order_history(self):
        if self.orders:
            for order in self.orders:
                print(order)
        else:
            print(f'No orders found for {self.name}')

# Example usage
appetizers_menu = Appetizers()
appetizers_menu.add_dish("Mozzarella sticks", 6.99)
appetizers_menu.add_dish("Bruschetta", 5.99)
appetizers_menu.view_menu()

entrees_menu = Entrees()
entrees_menu.add_dish("Spaghetti and meatballs", 12.99)
entrees_menu.add_dish("Chicken alfredo", 14.99)
entrees_menu.view_menu()

customer = Customers("John Doe", "123-456-7890")
customer.view_menu(appetizers_menu)
customer.place_order(appetizers_menu)
customer.place_order(entrees_menu)
customer.order_history()