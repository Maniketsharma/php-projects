"""
Iterable-__iter__or__getitem__()
iterater-__next__()
iteration-
"""
def gen(n):
    for i in range(n):
        yield i

g=gen(3)
'''print(g.__next__())
print(g.__next__())
print(g.__next__())'''
h= "345"
iter=iter(h)
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
"""for i in h:
    print(i)"""