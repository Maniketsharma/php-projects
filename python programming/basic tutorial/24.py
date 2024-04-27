'''#GLOATBLE VARIABLE OR GLOABLE KEYWORD
l=12#globle variable
def f(n):
    #l=5#local variable
    m=23
    global l
    print(l,m)
    print(n,"I HAVE PRINTED")

f("this is me")
print(m)'''

n=89
def harry():
    n=20
    def rohan():
        global n
        n=88
        print("Before call rohan()",n)
        rani()
        print("After calling rohan()",n)
        harry()
        print(n)

