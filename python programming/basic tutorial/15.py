#FUNCTION OR DOCSTRING
a=9
b=8
c=sum((a,b))#built in function
def func(a,b):
    print("hELLO URL FUNC",a+b)

    
def f(ac ,bc):
    """THIS IS A STRING WHICH CAN BE DEFINE AT THE CORTS IS CALLED DOCSTRING"""
    average = (ac+bc)/2
 #  print(average)
    return average
#v=f(5,6)
#print(v)
print(f.__doc__)
