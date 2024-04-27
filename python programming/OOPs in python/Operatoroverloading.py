#operatoroverloading and Dunder methode
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetail(self):
        return f"The name is {self.name}. Sallary is {self.salary} and Role is {self.role} "
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

        def __add__(self,other):
            return self.salary+other.salary
        def __truediv__(self,other):
                return self.salary/ other.salary
        def __repr__(self):
            return f"Employee({self.name},{self.salary},{self.role})"
        def __str__(self):
            return f"The name is {self.name}. Sallary is {self.salary} and Role is {self.role} "
emp1 = Employee("Harry",345,"Hacker")
#emp2 = Employee("Harry",300,"Cracker")
print(emp1)