#Decoratorin python
"""def fun1():
    print("Subscribed now vena goli mar dunga")
fun2=fun1
del fun1
fun2()
def funret(num):
    if num==0:
        return print
    if num==1:
        return sum
a=funret(1)
print(a)
def exect(f):
    f("this")
exect(print)"""
#Decorator in python function
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_me():
    print("I am chutiya ")

#who_is_me=dec1(who_is_me)

who_is_me()