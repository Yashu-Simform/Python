
class Employee:     #Declaration of Class named Employee
    """
    Base class for all employee \n
    constructor(fname,lname,salary,joining_date)
    """
    #Class Variables/Attribute
    emp_num = 0

    #constructor or init method
    def __init__(self, fname, lname, salary, joining_date):
        
        # Attributes
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.joining_date = joining_date
        pass

 
    # Methods
    def get_full_name(self):
        return self.fname + ' ' + self.lname
    

    # Class Methods
    @classmethod
    def set_emp_count(cls, value):
        cls.emp_num = value

    # Class method as alternate constructor
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, salary, joining_date = emp_str.split('-')
        return cls(fname, lname, salary, joining_date)
    

    #Static Methods
    @staticmethod
    def formatMsg(msg):
        return 'Message: ' + msg.lower() + '!'



emp1_det = ['Emp1', 'Emp1sur', 100000, "12/01/2025"]
emp2_det = ['Emp2', 'Emp2sur', 200000, "21/01/2025"]

emp1 = Employee(*emp1_det)
emp2 = Employee(*emp2_det)

def varUsage():
    # Usage of class variable and instance variables

    Employee.emp_num = 22
    emp1.emp_num = 22       #A new variable named emp_num is created in namespace of emp1 thus get its own copy
    print(Employee.emp_num)
    print(emp1.emp_num)
    print(emp2.emp_num)


def classMethodUsage():
    # Usage of class methods
    emp1.set_emp_count(100)
    print(Employee.emp_num)
    print(emp1.emp_num)
    print(emp2.emp_num)

def classMethod_as_alt_constructor():
    # Usage of class method as alternate constructor
    emp3_det = 'Emp3-Emp3Sur-30000-24/01/2025'

    emp3 = Employee.from_string(emp3_det)
    print(dir(emp3))


def usageStaticMethod():
    # Usage of Static Methods
    msg = Employee.formatMsg('Hi this is working day')
    print(msg)

    msg1 = emp1.formatMsg('This is emp1.')
    print(msg1)