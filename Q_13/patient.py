from Q_13.person import Person


class Patient(Person):
    def __init__(self, name, age, medical_history):
        super().__init__(name, age)
        self.__medical_history = medical_history

    def get_details(self):
        return f"Patient {super().get_details()}, Medical History: {self.__medical_history}"
