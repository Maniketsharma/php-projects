class A:
    classvar1="I am in class vaiable A"
    def __init__(self):
        self.var1 ="I inside in a Class A' as constuctor"
        self.classvar1="Instance of Var in class A"
        self.special="Special"
class B(A):
    pass
    classvar1="I am class B"
    def __init__(self):
        self.var1 = "I inside in a Class B' as constuctor"
        self.classvar1 = "Instance of Var in class B"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
print(a.special,a.var1,b.classvar1)
print(b.special,b.var1,b.classvar1)