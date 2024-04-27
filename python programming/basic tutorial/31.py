#Enumerate in python:
l1 = ["Bhindi","Aloo","chosticks","chowlwin"]
"""i=1
for iter in l1:
    if i%2 != 0:
        print(f"jarvise Please buy  {l1}")
    i += 1"""
for index, item in enumerate(l1):
    if index%2==0:
        print(f"jarvise Please buy {item}")
