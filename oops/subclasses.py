from oops import Employee

class Developer(Employee):
    def __init__(self, *emp_Det, dept):
        super().__init__(*emp_Det)
        print(super().get_full_name())
        self.dept = dept
        pass

    def get_details(self):
        print('Name:', self.fname, self.lname,sep=' ',end='\n')
        print('Salary: ',self.salary)
        print('Joining date: ', self.joining_date)

dev1 = Developer(*["Yashu", "Ranparia", 550000, '06/01/2025'], dept='Python')

dev1.get_details()

# print(help(dev1))

Developer.emp_num = 15
Employee.emp_num = 20
dev1.emp_num = 25
Developer.emp_num = 155
print(Employee.emp_num)
print(dev1.emp_num)