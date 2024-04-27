class employee:
    no_of_leaves=8
harry=employee()
larry=employee()
harry.name="Harry"
harry.salary=4500000
harry.role="sinior Software Enginier"
larry.name="Larry"
larry.salary=4000000
larry.role=" junior Software Enginier"
print(larry.no_of_leaves)
print(larry.__dict__)
print(employee.__dict__)
employee.no_of_leaves=9
print(harry.__dict__)
print(employee.__dict__)
print(employee.no_of_leaves)
print(harry.name,harry.salary,harry.role)
