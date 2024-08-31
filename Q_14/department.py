class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def add_employee(self, emp_name):
        self.employees.append(emp_name)

    def display_department(self):
        employees = ", ".join(self.employees)
        return f"Department: {self.dept_name}, Employees: {employees}"
