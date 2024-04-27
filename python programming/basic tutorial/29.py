#**Args,**Kwargs in python
#ARGS
#def d_n_print(a,b,c,does.txt,e):
 #   print(a,b,c,does.txt,e)

def args(normal,*argsCAMMY,**kwargs):
    print(normal)
    for item in argsCAMMY:
       print(item)
       print("\nNow i will introduces to my gareeb friend")
       for key, value in kwargs.items():
           print(f"{key}is a ,{value}")
           
#d_n_print("HAMY","CAMMY","SKIM","TELE","LDFS")
h=["HAMY","CAMMY","SKIM","TELE","LDFS","the aprogrsammer"]
normal="I AM A NORMAL ARGUMENT WHICH STUDENT ARE"
k={"Rohan":"Monior","maty":"imstructor","jety":"procoder in python"}
args(normal,*h,**k)
#Kwargs
