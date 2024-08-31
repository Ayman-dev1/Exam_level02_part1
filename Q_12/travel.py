from abc import ABC, abstractmethod


class TravelPackage(ABC):

    @abstractmethod
    def calc_total_cost(self):
        pass

    @abstractmethod
    def display_package_cost(self):
        pass
