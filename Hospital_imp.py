class Patient:
    def __init__(self, id, name, malady):
        self.id = id
        self.name = name
        self.malady = malady


class Hospital:
    def __init__(self, name, capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity

    def add(self, patient):
        if len(self.patients) >= self.capacity:
            print(f'Sorry {patient.name}! The Hospital is full!')
        else:
            patient_dictionary = {
            'ID': patient.id,
            'Name': patient.name,
            'malady': patient.malady,
            }
            self.patients.append(patient_dictionary)
            print(f'{patient.name} has been admitted.')
            
    def discharge(self, name):
        for value in self.patients:
            if value['Name'] == name:
                self.patients.remove(value)
        print(f'{name} discharged')


patient1 = Patient(1, 'Ann', 'Allergies')
patient2 = Patient(2, 'Bob', 'Stomach Aches')
patient3 = Patient(3, 'Mark', 'Headache')
patient4 = Patient(4, 'Andre', 'Colds and Flu')
hospital = Hospital('Hospital', 3)
hospital.add(patient1)
hospital.add(patient2)
hospital.add(patient3)
hospital.add(patient4)
hospital.discharge('Ann')
hospital.discharge('Mark')
hospital.add(patient4)
