'''public-data view by anu persion in public methode
private- data view by persionaldata
protected-data secured by persion
'''
class Employee:
    var=8
    no_of_leaves = 8
    _protect=9
    __private=98
    def __init__(self , aname, asalary, asrole):
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

emp=Employee("harry",67000,"Hacker for code")
print(emp._protect)
print(emp._Employee__private)