from Q_12.travel import TravelPackage


class TourPackage(TravelPackage):
    def __init__(self, days, cost_per_day):
        self.__days = days
        self.__cost_per_day = cost_per_day

    def calc_total_cost(self):
        return self.__days * self.__cost_per_day

    def display_package_cost(self):
        total_cost = self.calc_total_cost()
        discount_cost = total_cost - (total_cost * 10/100)
        print('Total Cost for Tour Package After 10% Discount', '$', discount_cost)
