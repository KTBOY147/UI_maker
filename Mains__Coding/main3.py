class Person:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def printname(self):
        print(self.name, self.lname)

class Employee(Person):
    pass

x = Employee("Subodh", "Thakur")
x.printname()
