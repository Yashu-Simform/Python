import unittest
from oops.oops import Employee

class TestClass(unittest.TestCase):

    def setUp(self):
        print('Initializing test methods!')
        self.emp1 = Employee('Yashu', 'Ranparia', 1000000, '06/01/2025')
        self.emp2 = Employee('Chota', 'Don', 5000, '08/01/2025')
        # return super().setUp()
    
    def tearDown(self):
        print('Test Method Ended!')
        # return super().tearDown()

    def test_emp_update(self):
        self.assertEqual(self.emp1.fname + ' ' + self.emp1.lname, self.emp1.get_full_name())