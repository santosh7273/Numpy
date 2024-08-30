import numpy as np
li=[1,'world',22] #it occupies more memory so numpy will be used
print(li)
np1=np.array([1,2,3])
print(np1)
#numpy should contain same datatype elements
#however we can insert diifernt datatypes uisng dtype keyword
print(np1.shape) #used to find the length of np array like len funtion of lists
np2=np.arange(5) #used to print values from 0 to n-1
print(np2)
np3=np.arange(1,5,2) #with step count with start and end+1 values also
print(np3)
print(np3.ndim,np3.nbytes) # used to find the dimesion and memory size occupied by numpy array
np4=np.zeros(10) # used to fill n zeroes
print(np4) 
np5=np.zeros((2,10))
print(np5)
np6=np.full((10),2) # used to fill np array with any number
print(np6)
np7=np.full((2,10),7)
print(np7)
print(li)
np8=np.array(li)
print(np8)
print(np2[3])
