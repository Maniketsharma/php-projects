class Employee:
    no_of_leaves = 8
    def __init__(self , aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetail(self):
        return f"The name is {self.name}. Sallary is {self.salary} and Role is {self.role} "\

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(str):
        print("This is too good "+ str)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan",455,"Student")
karan=Employee.from_dash("Karan-480-student")

Employee.printgood("324325324")
rohan.printgood("Rohan")
harry.printgood("Harry")