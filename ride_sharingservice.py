from abc import ABC, abstractmethod


class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info


class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_capacity(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.capacity = 4

    def get_capacity(self):
        return self.capacity


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.capacity = 1

    def get_capacity(self):
        return self.capacity


class Driver(User):
    def __init__(self, name, contact_info, vehicle):
        super().__init__(name, contact_info)
        self.vehicle = vehicle
        self.rating = None

    def accept_ride(self, ride):
        if ride.driver is None and ride.passenger is not None and self.vehicle.get_capacity() >= 1:
            ride.driver = self
            return True
        else:
            return False

    def complete_ride(self, ride):
        if ride.driver == self and ride.passenger is not None:
            ride.completed = True
            return True
        else:
            return False


class Passenger(User):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.rating = None

    def request_ride(self, destination):
        ride = Ride(self, None, destination, None)
        return ride


class Ride:
    def __init__(self, passenger, driver, destination, fare):
        self.passenger = passenger
        self.driver = driver
        self.destination = destination
        self.fare = fare
        self.completed = False

    def rate_driver(self, rating):
        if self.driver is not None:
            self.driver.rating = rating

    def rate_passenger(self, rating):
        if self.passenger is not None:
            self.passenger.rating = rating


class RideSharing(ABC):
    @abstractmethod
    def search_driver(self, destination):
        pass

    @abstractmethod
    def accept_ride(self, ride, driver):
        pass

    @abstractmethod
    def complete_ride(self, ride, driver):
        pass

    @abstractmethod
    def rate_user(self, user, rating):
        pass


class Uber(RideSharing):
    def __init__(self):
        self.drivers = []
        self.rides = []

    def search_driver(self, destination):
        for driver in self.drivers:
            if driver.accept_ride(Ride(None, None, destination, None)):
                return driver
        return None

    def accept_ride(self, ride, driver):
        if driver.complete_ride(ride):
            ride.fare = 10  # Assume a flat fare of $10 for simplicity
            self.rides.append(ride)
            return True
        else:
            return False

    def complete_ride(self, ride, driver):
        if ride in self.rides and driver.complete_ride(ride):
            return True
        else:
            return False

    def rate_user(self, user, rating):
        user.rating = rating


# Create drivers and passengers
car1 = Car("Toyota", "Camry", 2010)
driver1 = Driver("Alice", "alice@example.com", car1)
car2 = Car("Honda", "Accord", 2015)
driver2 = Driver("Bob", "bob@example.com", car2)
passenger1 = Passenger("David", "david@example.com")
passenger2 = Passenger("Emily", "emily@example.com")

# Create ride-sharing service and add drivers
uber = Uber()
uber.drivers.extend([driver1, driver2])

# Passengers request rides
ride1 = passenger1.request_ride("Airport")
ride2 = passenger2.request_ride("Mall")

# Drivers accept and complete rides, and rate each other
if uber.accept_ride(ride1, uber.search_driver("Airport")):
    uber.complete_ride(ride1, driver1)
    ride1.rate_driver(5)
    ride1.rate_passenger(4)

if uber.accept_ride(ride2, uber.search_driver("Mall")):
    uber.complete_ride(ride2, driver2)
    ride2.rate_driver(4)
    ride2.rate_passenger(5)

# Print ratings
print("Driver", driver1.name, "rating:", driver1.rating)
print("Driver", driver2.name, "rating:", driver2.rating)
print("Passenger", passenger1.name, "rating:", passenger1.rating)
print("Passenger", passenger2.name, "rating:", passenger2.rating)
