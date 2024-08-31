#main Program
from Q_13.doctor import Doctor
from Q_13.patient import Patient


def display_person_details(person):
    print(person.get_details)


patient = Patient(name="Omar", age=30, medical_history="Hypertension")
doctor = Doctor(name="Dr. Hesham", age=45, speciality="Cardiology")

display_person_details(patient)
display_person_details(doctor)
