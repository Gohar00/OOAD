from abc import ABC, abstractmethod


class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def set_make(self, make):
        self.make = make

    def get_make(self):
        return self.make

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def display_info(self):
        return [self.make, self.model, self.price]

    def get_type(self):
        pass


class ElectricCar(Car):
    def __init__(self, make, model, price, battery):
        super().__init__(make, model, price)
        self.battery = battery

    def set_battery(self, battery):
        self.battery = battery

    def get_battery(self):
        return self.battery

    def get_type(self):
        return "Electric"


class HybridCar(Car):
    def __init__(self, make, model, price, fuel):
        super().__init__(make, model, price)
        self.fuel = fuel

    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_fuel(self):
        return self.fuel

    def get_type(self):
        return "Hybrid"


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact

    def search(self, car_list, make=None, model=None, cartype=None, max_price=0, min_price=0):
        results = []
        for car in car_list:
            if make and car.get_make() != make:
                continue
            if model and car.get_model() != model:
                continue
            if cartype and car.get_type() != cartype:
                continue
            if (max_price <= car.price) and (min_price >= car.price):
                continue
            results.append(car)
        return results

    def purchase(self, car, salesperson):
        price = car.get_price()
        commission_rate = salesperson.get_commission()
        commission = price * commission_rate / 100
        total_price = price + commission
        return "Purchase successful. Total price: ${:.2f}".format(total_price)


class SalesOperation(ABC):

    @abstractmethod
    def add_car(self, car):
        pass

    @abstractmethod
    def remove_car(self, car):
        pass


class SalesPeople(SalesOperation):
    def __init__(self, people_name, commission_rate):
        self.people_name = people_name
        self.commission_rate = commission_rate
        self.car_inventory = []
        self.sales_history = []

    def set_peoplename(self, people_name):
        self.people_name = people_name

    def get_peoplename(self):
        return self.people_name

    def set_commission(self, commission_rate):
        self.commission_rate = commission_rate

    def get_commission(self):
        return self.commission_rate

    def add_car(self, car):
        self.car_inventory.append(car)

    def remove_car(self, car):
        self.car_inventory.remove(car)

    def make_sale(self, customer, car):
        price = car.get_price()
        commission_rate = self.get_commission()
        commission = price * commission_rate / 100
        total_price = price + commission
        sale = {'salesperson': self.get_peoplename(), 'customer': customer.get_name(),
                'car': car.display_info(), 'price': price, 'commission': commission, 'total_price': total_price}
        self.sales_history.append(sale)
        return "Sale successful. Total price: ${:.2f}".format(total_price)

    def view_history(self):
         print(self.sales_history)


# client code
car1 = ElectricCar("Tesla", "Model5", 800000, 100)
car2 = ElectricCar("Nissan", "Model3", 400000, 60)
car3 = HybridCar("Toyota", "Prius", 30000, 50)
car4 = HybridCar("Toyota", "JJJ", 50000, 70)

salesperson1 = SalesPeople("Jack", 5)
salesperson2 = SalesPeople("Artak", 4)

salesperson1.add_car(car4)
salesperson1.add_car(car3)
salesperson2.add_car(car1)
salesperson2.add_car(car2)
salesperson2.add_car(car3)

customer1 = Customer("Ani", "student")
customer2 = Customer("Aram", "developer")

results = customer1.search(salesperson1.car_inventory, make="Toyota", cartype="Hybrid", max_price=90000)
print("Search result: ")
for car in results:
    print(car.display_info())

purchase_result = customer1.purchase(results[0], salesperson1)
print(purchase_result)

salesperson1.make_sale(customer1, results[0])
salesperson1.view_history()
