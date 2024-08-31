from Q_13.person import Person


class Doctor(Person):
    def __init__(self, name, age, speciality):
        super().__init__(name, age)
        self.__speciality = speciality

    def get_details(self):
        return f"Doctor {super().get_details()}, Speciality: {self.__speciality}"
