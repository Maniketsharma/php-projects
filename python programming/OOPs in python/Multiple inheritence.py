#Multiple inheritence
class Employee:
    var=8
    no_of_leaves = 8
    def __init__(self , aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

        def print_detail(self):
            return f"The name is {self.name}. Sallary is {self.salary} and Role is {self.role} "

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(str):
        print("This is too good "+ str)
class player:
    var=4
    no_of_game=4
    def __init__(self , name, game):
        self.name = name
        self.game = game
        def print_detail(self):
            return f"The name is {self.name}. Game is {self.game} "

class Coolprogrammer(Employee,player):
        var=10
        language="C++"
        def lang(self):
            print(self.lang)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan",455,"Student")

shubha=player("Shubha",["Free fire player"])
karan= Coolprogrammer("Karan",4500,"Free Fire player")
#det=karan.print_detail()
#print(det)
print(karan.var)