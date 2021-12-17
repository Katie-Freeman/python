import unittest
from employee_raise import Employee

class EmployeeRaiseTest(unittest.TestCase): 
    
    def setUp(self):
        print("SETUP")
        self.employee = Employee("John Doe", 45000)
    
    def test_give_raise(self):
        self.employee.give_raise(5000)
        self.assertEqual(30000, self.employee.salary)

    def tearDown(self):
        print("TEARDOWN")

if __name__ == '__main__':
    unittest.main()
