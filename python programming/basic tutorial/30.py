#Time module in python
import time
initial=time.time()

k=0
while(k<45):
    print("THis is harry bhai")
    k+=1
    time.sleep(2)
    print("while loopran in",time.time()-initial,"Second")
initial2=time.time()
for i in range(45):
        print("THis is harry bhai")
        print("for loop ran in",time.time()-initial2,"Second")
        
#localtime=time.asctime(time.localtime(time.time()))
#print(localtime)
