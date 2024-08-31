class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}"


