import numpy as np 

x=np.array([[1,2],[3,9]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)

print(x+y)
print(np.add(x,y))


arr1 = [[1,3],[4,6]]
arr2 = [[3,5],[3,8]]
print (arr1 + arr2)
print(np.add(arr1,arr2))