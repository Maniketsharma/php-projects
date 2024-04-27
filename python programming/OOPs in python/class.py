# Class and oblects in python :
"""
in the python class are basically Templates which can be define as a contaioner name which are many objectarestored and working
in this container
for example= Class - Template
Object- instance of the class //Catagory of class--dry=do not repeat yourself
for example - get_no_of_films(table)"""
class Std:
    pass

harry=Std()
larry=Std()

harry.name="Harry"
harry.std=12
harry.section=1
larry.std=2
larry.subject=["hindi","physics"]
print(harry.name,harry.section,larry.std,larry.subject)
print(harry,larry)
