import numpy as np
np1=np.array([1,2,3,4])
np2=np1.view()
print(np1)
print(np2)
np1[0]=22
print(np1)
print(np2)
np3=np.array([1,2,3])
np4=np3.copy()
np3[0]=2323
print(np3)
print(np4)