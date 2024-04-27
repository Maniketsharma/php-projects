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
          self.fname = None
          self.lname = None
suzuki_hayabusa = Employee("suzuki", "hayabusa")
print(suzuki_hayabusa.email)
suzuki_hayabusa.fname = "US"
print(suzuki_hayabusa.email)
suzuki_hayabusa.email = "this.that@codewithhaarry.com"
print(suzuki_hayabusa.email)

del suzuki_hayabusa.email
print(suzuki_hayabusa.email)
suzuki_hayabusa.email = "Harry.MArry@codewithhaarry.com"
print(suzuki_hayabusa.email)