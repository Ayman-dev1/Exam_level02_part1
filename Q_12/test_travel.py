# main Program
from Q_12.hotel import HotelPackage
from Q_12.tour import TourPackage

hotel_package = HotelPackage(5, 200)
tour_package = TourPackage(7, 100)


hotel_package.display_package_cost()
tour_package.display_package_cost()
