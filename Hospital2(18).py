from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class Appointments:

    def __init__(self, patient, doctor, procedure):
        pass



class InPersonAppointment(ABC):

    @abstractmethod
    def manage_appointments(self):
        pass

class VirtualAppointment(ABC):

    @abstractmethod
    def manage_appointments(self):
        pass


class Patient(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.medical_history = []

    def add_to_history(self, procedure):
        self.medical_history.append(procedure)


class Doctor(Person):
    def __init__(self, name, contact, speciality):
        super().__init__(name, contact)
        self.speciality = speciality


