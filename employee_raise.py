class Employee:
    def __init__(self, employee_name, annual_salary):
        self.employee = employee_name
        self.salary = annual_salary 
    
    def give_raise(self, amount=5000):
        self.salary += amount

