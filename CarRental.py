from abc import ABC, abstractmethod

class Rental(ABC):
    @abstractmethod
    def rent(self, customer, duration):
        pass

    @abstractmethod
    def return_car(self, customer):
        pass

class Car(ABC):
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.rental_price = rental_price

    @abstractmethod
    def get_type(self):
        pass

class LuxuryCar(Car):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def get_type(self):
        return "Luxury"

class EconomyCar(Car):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def get_type(self):
        return "Economy"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []
        self.rentals = []

    def rent_car(self, rental, duration):
        rental.rent(self, duration)

    def return_car(self, rental):
        rental.return_car(self)
        self.rental_history.append(rental)

    def search_cars(self, car_list, car_type):
        available_cars = []
        for car in car_list:
            if car.get_type() == car_type and car not in self.rentals:
                available_cars.append(car)
        return available_cars

    def view_rental_history(self):
        rental_history = []
        for rental in self.rentals:
            rental_history.append((rental.car.make, rental.car.model, rental.duration, rental.returned))
        return rental_history


class RentalCar(Rental):
    def __init__(self, car):
        self.car = car
        self.is_rented = False
        self.rented_by = None
        self.rental_duration = 0

    def rent(self, customer, duration):
        if self.is_rented:
            print("Sorry, this car is already rented.")
        else:
            self.is_rented = True
            self.rented_by = customer
            self.rental_duration = duration
            print(f"{self.car.make} {self.car.model} has been rented by {customer.name} for {duration} days at {self.car.rental_price} per day.")

    def return_car(self, customer):
        if not self.is_rented:
            print("This car is not rented.")
        elif self.rented_by != customer:
            print("You did not rent this car.")
        else:
            self.is_rented = False
            self.rented_by = None
            self.rental_duration = 0
            print(f"{self.car.make} {self.car.model} has been returned by {customer.name}.")



luxury_car1 = LuxuryCar("Mercedes-Benz", "S-Class", 250)
luxury_car2 = LuxuryCar("BMW", "7 Series", 200)
economy_car1 = EconomyCar("Toyota", "Corolla", 100)
economy_car2 = EconomyCar("Honda", "Civic", 90)

car_list = [luxury_car1, luxury_car2, economy_car1, economy_car2]

customer1 = Customer("John", "john@example.com")
customer2 = Customer("Jane", "jane@example.com")


available_cars = customer1.search_cars(car_list, "Luxury")
print(f"Available luxury cars: {[car.make + ' ' + car.model for car in available_cars]}")

rental_car = RentalCar(available_cars[0])
customer1.rent_car(rental_car, 7)

available_cars = customer2.search_cars(car_list, "Economy")
print(f"Available economy cars: {[car.make + ' ' + car.model for car in available_cars]}")

rental_car = RentalCar(available_cars[0])
customer2.rent_car(rental_car, 5)

customer1.return_car(rental_car)

customer2.return_car(rental_car)

rental_history = customer1.view_rental_history()
print(f"John's rental history: {rental_history}")

rental_history = customer2.view_rental_history()
print(f"Jane's rental history: {rental_history}")
