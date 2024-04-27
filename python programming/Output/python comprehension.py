#ls=[]
#for i in range(200):
 #   if i%3==0:
  #      ls.append(i)

#ls=[i for i in range (100) if i%3==0]
#print(ls)


#dict = {i:f"item{i}" for i in range(5)}
#dict2={value:key for key,value in dict.items()}
#print(dict,dict2)


#dress1=[dress for dress in ["d1","d1","d2","d1","d2","d1","d2","d2","d1"]]
#print(type(dress1))

even=(i for i in range (100)if i%2==0)
#print(even.__next__())
for item in even:
    print(item)