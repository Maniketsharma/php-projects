#Inheritence : inheritence is a methode which can add or inherite one class to another class
#it can be define as three types: Single inheritence
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
class prog(Employee):
    no_of_holiyday=100
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage

    def printprog(self):
       return f"The Programmer is {self.name}.\nSallary{45000} \nand role is {self.role}.\nThe languages are {self.language}"
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan",455,"Student")

Shubham=prog("SHunbham",45000,"prog",["python"])
karama= prog("Karma",67000,"prog",["python","c++","Java"])
print(karama.printdetail())
print(karama.printprog())
print(karama.no_of_holiyday)