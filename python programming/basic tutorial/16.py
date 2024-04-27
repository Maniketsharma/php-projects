#TRY EXECPT EXECPTION HANDLING
print("Enter the number 1")
n1=input()
print("Enter the number 2")
m1=input()
try:
    print("Sum of  the two number are:",int(n1)+int(m1))
except Exception as e:
    print(e)


    
    print("This line is very important")
