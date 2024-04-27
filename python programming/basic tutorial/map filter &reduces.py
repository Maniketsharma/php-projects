#n=["3","43","345","34"]
#n=list(map(int,n))
#for i in range(len(n)):
 #   n[i]=int( n[i])
#n[2]=n[2]+1
#print(n[:2])
#print(n[:2])
def sq(a):
    return a*a
def cutta(a):
    return a*a*a
func=[sq,cutta]
#num=[2,44,56,443,243,5,65]
#for i in range(5):
#   val=list(map(lambda x:x(i),func))
#   print(val)
#------------filter------------------------
'''list1=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
        return num>5
gt_than_5=list(filter(is_greater_5,list1))
print(gt_than_5)'''
#------------------------reduces----------
from functions import reduce

list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
num=0
for i in list1:
    num=num+i
    print(num)