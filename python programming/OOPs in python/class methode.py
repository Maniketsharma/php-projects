class Employee:
    no_of_leaves = 8
    def __init__(self , aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetail(self):
        return f"The name is {self.name}. Sallary is {self.salary} and Role is {self.role} "\

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan",455,"Student")

harry.change_leaves(34)
Employee.change_leaves(124)
print(harry.no_of_leaves)