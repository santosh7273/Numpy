import numpy as np
np1=np.array([1,2,3,4,2,3,4])
print(np1)
if 3 in np1:
    print(3)
x=np.where(np1==3)
print(x[0])
y=np.where(np1%2==0)
print(y[0])
print(np1[y[0]])