from Q_11.vacation import VacationPackage


class RelaxationPackage(VacationPackage):
    def __init__(self, destination, price, spa_services):
        super().__init__(destination, price)
        self.__spa_services = spa_services

    def display_details(self):
        super().print_vacation_details()
        print('Spa Services:', self.__spa_services)
