class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

    def Name(self):
        return self.firstname + " " + self.lastname + " "+self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())
print(y.Name())

# Python example to check if a class is
# subclass of another

class Base(object):
    pass   # Empty Class

class Derived(Base):
    pass   # Empty Class

# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print("This is an instance of Derived Class %s" %isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))

class Employee:
    """Common base class for all employees"""
    # static variable
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    @staticmethod
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    @classmethod
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("amir riaz", 40)
print(emp1.empCount)
emp2 = Employee("Kashif riaz", 30)
print(emp1.empCount)

print(Employee.empCount)