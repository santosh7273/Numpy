import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)
np2=np1.reshape(3,3)
print(np2)
print(np2.shape)
np3=np2.reshape(-1)
print(np3,np3.shape)