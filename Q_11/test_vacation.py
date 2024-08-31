# main program
# display Vacation Packages
from Q_11.adventure import AdventurePackage
from Q_11.relaxation import RelaxationPackage

adventure = AdventurePackage('Turkey', 2500, ['Hiking', 'Rafting'])
relaxation = RelaxationPackage('Red Sea', 3000, ['Massage', 'Yoga'])


adventure.display_details()
print('---------')
relaxation.display_details()
