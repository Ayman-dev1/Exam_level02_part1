from abc import ABC


class Calculator(ABC):
    def __init__(self, model_name, color, length, width):
        self.__model_name = model_name
        self.__color = color
        self.__length = length
        self.__width = width

    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        return a - b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

    @staticmethod
    def divide_numbers(a, b):
        return a / b




