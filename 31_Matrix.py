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

# =========================================================
#  --  matrix format:
# =========================================================

arr1 = array([
    [1, 2, 3, 4],
    [4, 5, 6, 7]
])
print("normal array")
print(arr1)
print("matrix")
m = matrix(arr1)
print(m)

# other way to create matrix:
print("create maxtrix without using array 2 r 4 col")
m = matrix('1 2 3 4 ; 5 6 7 8')
print(m)

print("create maxtrix 4 r 2 col")
k = matrix('1 2 ;3 4 ; 5 6 ;7 8')
print(k)


print("create maxtrix 3 r 3 col")
k = matrix('1 2 3; 4 5 6 ;7 8 0')
print(k)

print("Diagonal of prev matrix")
print(diagonal(k))

print("Diagonal of prev matrix")
print(diagonal(k))

print("max of matrix", k.max())
print("min of matrix", k.min())


print('---------------------')

m1 = matrix('1 2 3; 4 5 6 ;7 8 0')
m2 = matrix('1 2 3; 4 5 6 ;7 8 0')

m3 = m1 + m2
print('sum of 2 mat', m3)

m3 = m1 * m2
print('* of 2 mat', m3)
