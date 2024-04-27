import pickle
#Pickling module use in pythone object
cars=["BMw","AUDI","MARUTI","SUZUKI","HONDA","HYUNDAI","TATA","TOYTA"]
file="mycar.pkl"
fileobj= open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))
