from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name


class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.medical_procedure = []

    def add_to_history(self, procedure):
        self.medical_procedure.append(procedure)

    def display_info(self):
        print(f"Patient name: {self.name}")
        print(f"Patient age: {self.age}")
        print(f"Patient medical history: {','.join(self.medical_procedure)}")


class MedicalStaff(Person):

    def __init__(self, name, position):
        super().__init__(name)
        self.position = position
        self.surgery_schedule = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

    def manage_hospital_operation(self, doctor, day):
        if doctor in [doc for day in self.surgery_schedule.values() for doc in day]:
            print("Doctor already scheduled for surgery on another day.")
        if doctor in self.surgery_schedule[day]:
            print("Doctor already scheduled for surgery on this day.")
            return
        self.surgery_schedule[day].append(doctor)


class Doctor(MedicalStaff):
    def __init__(self, name, contact):
        super().__init__(name, "Doctor")
        self.contact = contact
        self.appointments = {}
        self.patients = {}

    def manage_patient_info(self, patient):
        self.patients[patient.name] = [f'age: {patient.age}, patient_history: {patient.medical_procedure}']

    def manage_appointment(self, patient, day):
        appointment_key = f"{day}"
        if appointment_key in self.appointments:
            print("Appointment already booked. Please choose a different time.")
        else:
            self.appointments[appointment_key] = patient.name


class MedicalProcedure(ABC):

    @abstractmethod
    def perform(self, patient):
        pass


class Surgery(MedicalProcedure):
    def __init__(self, surgeon, procedure):
        self.surgeon = surgeon
        self.procedure = procedure

    def perform(self, patient):
        patient.add_to_history(self.procedure)
        return f"{patient.name} underwent {self.procedure} performed by {self.surgeon}"


class CheckUp(MedicalProcedure):
    def __init__(self, check_name):
        self.check_name = check_name

    def perform(self, patient):
        patient.add_to_history(self.check_name)
        return f"{patient.name} underwent {self.check_name} check-up"


p1 = Patient("Jack", 23)
p2 = Patient("Mari", 30)
d1 = Doctor("Dr. Smith", "99123456")

d1.manage_hospital_operation(d1.name, "Monday")
d1.manage_appointment(p1, "Monday")

surgery = Surgery(d1.name, "appendectomy")
print(surgery.perform(p1))

checkup = CheckUp("blood pressure")
print(checkup.perform(p1))

d1.manage_patient_info(p1)

print(d1.appointments)
