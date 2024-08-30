import numpy as np
np1=np.array([1,2,3,4])
for i in np1:
    print(i)
np2=np.array([[1,2,3],[4,5,6]])
for i in np2:
    for j in i:
        print(j)
print(len(np1))
np3=np.array([11,12,1,3])
for i in np.nditer(np3):
    print(i)