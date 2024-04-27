class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
         return f"This is an Employee is {self.fname} {self.lname}"


    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set please reset it..."
        return f"{self.fname}.{self.lname}@codewithharry.com"


    @email.setter
    def email(self, string):
        print("Setting now.......")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]


    @email.deleter
    def email(self):
          self.fname= None
          self.lname= None

skillf=Employee("Skill","F")
o="this is  a o object"
#print(skillf.email)
#print(id("This os a srting"))
#print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))