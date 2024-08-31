from abc import ABC, abstractmethod


class VacationPackage(ABC):
    def __init__(self, destination, price):
        self.__destination = destination
        self.__price = price

    def print_vacation_details(self):
        print('Destination:', self.__destination)
        print('Price:', self.__price)

    @abstractmethod
    def display_details(self):
        pass
