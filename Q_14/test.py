from Q_14.hrd_department import HRDepartment
from Q_14.technical_department import TechnicalDepartment

# main program
tech_dept = TechnicalDepartment("Tech")
hr_dept = HRDepartment("HR")

tech_dept.add_employee("Alice")
tech_dept.add_employee("Bob")
hr_dept.add_employee("Charlie")

print(tech_dept.display_department())
print(hr_dept.display_department())
