'''#WRITING AND APPENDING TO FILE
f= open("p2.txt","w")
a=f.write("Hartt fdkjshfjksdkl\n")
print(a)
f.close()
'''
#HANDLE READ AND WRITEMODES
f=open("p2.txt","r+")
print(f.read())
f.write("Thank you")
