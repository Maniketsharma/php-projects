#Self or __intit__()(constructor in oops)
class sd:
    no_of_leaves=8
    def __init__(self ,aname ,asalary ,arole ,aage):
        self.name=aname
        self.age = aage
        self.salary=asalary
        self.position = arole


    def printinformation(self):
        return f"\nName is {self.name}. \nAge is {self.age}. \nSallary is {self.salary} and \nRole is {self.position} "
mani = sd("Maniket Sharma",21, 4000000, "Sinior software developer")
'''mani=sd()
ani=sd()
mani.name="Maniket Sharma"
mani.age=23
mani.sallary=1203550000
mani.position="Sinior Software enginieer"
print(mani.printinformation())
ani.name="Aniket verma"
ani.age=24
ani.sallary=103550000
ani.position="Juniour Software enginieer"
print(ani.printinformation())
print(mani.no_of_leaves)
print(ani.no_of_leaves)'''
print(mani.name,mani.age,mani.salary,mani.position)