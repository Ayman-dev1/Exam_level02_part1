from Q_12.travel import TravelPackage


class HotelPackage(TravelPackage):
    def __init__(self, nights, cost_per_night):
        self.__nights = nights
        self.__cost_per_night = cost_per_night

    def calc_total_cost(self):
        return self.__nights * self.__cost_per_night

    def display_package_cost(self):
        total_cost = self.calc_total_cost()
        print('Total Cost for Hotel package:', '$', total_cost)
