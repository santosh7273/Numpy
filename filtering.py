import numpy as np
np1=np.array([3,4,2,1])
print(np1)
np2=[True,False,False,True]
print(np2)
print(np1[np2])
#filtering all the even numbers
np4=np.array([45,32,43,22,778])
x=list()
for i in np4:
    if i%2==0:
        x.append(True)
    else:
        x.append(False)
print(x)
print(np4[x])
print(np4)
li=np4%2==0
print(np4[li])
li2=np4>=5
print(np4[li2])