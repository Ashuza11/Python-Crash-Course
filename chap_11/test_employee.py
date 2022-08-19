"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 11-3. Employee
import unittest

from employee import Employee

class EmployeeTest(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """Create an employee to use in test."""
        self.employee_one = Employee('john', 'Aganze', 10000)


    def default_raise(self):
        """Test for the default raise"""
        self.employee_one.give_raise()
        self.assertEqual(self.employee_one.anual_salary, 15000)

    def test_give_custom_raise(self):
        """Test for the customised raise"""
        self.employee_one.give_raise(2000)
        self.assertEqual(self.employee_one.anual_salary, 12000)
        
unittest.main()