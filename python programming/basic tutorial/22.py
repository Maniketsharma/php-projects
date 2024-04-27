#USING BLOCK TO OPEN PYTHON FILES
with open("mni.txt")as f:
    a =f.readlines()
    print(a)
f=open("mni.txt","rt")
print(f.readline())
f.close()

