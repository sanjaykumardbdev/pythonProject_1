from numpy import *

arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr1)
print(arr1.dtype)

# extract 1d from multi dimentional array
arr1d = arr1[0]
arr2d = arr1[1]
print(arr1d, arr2d)

#print all together in one line
print("all in one line")
arrone = arr1.flatten()
print(arrone)
print()

print("3 dimemsional array")

arr1 = array([
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9]
])
print(arr1)
print(arr1.dtype)

arr3 = arr1.reshape(3, 4)  # 2 dim : 3 rows and 4 column
print("2dim")
print(arr3)

# 2 dim : 2 2d array , each 2d array have 2 1d array , each 1d have 3 val
arr3 = arr1.reshape(2, 2, 3)
print("3dim")
print(arr3)
