from Q_11.vacation import VacationPackage


class AdventurePackage(VacationPackage):
    def __init__(self, destination, price, activities):
        super().__init__(destination, price)
        self.__activities = activities

    def display_details(self):
        super().print_vacation_details()
        print('Activities:', self.__activities)
