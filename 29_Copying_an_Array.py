from numpy import *

arr = array([1, 2, 3, 4, 5])
arr = arr + 2
print(arr)

# Vectorized array
arr1 = array([1, 2, 3, 4, 25])
arr2 = array([1, 2, 3, 4, 25])
arr3 = arr1 + arr2
print(arr3)

print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print('------------')
print(min(arr1))
print(max(arr1))
print(sqrt(arr1))

print('------------')
print(sort(arr1))
print(concatenate([arr1,arr2]))

print('------------ copy arr into another array')
# creating alias of an array, address will be same
arr6 = array([3, 4, 5, 6, 7])
arr7 = arr6

print(arr6, id(arr6))
print(arr7, id(arr7))

print('------------ copy arr into another array but different address')
arr3 = array([1, 2, 3, 4, 5])
arr4 = arr3.view()

print(arr3, id(arr3))
print(arr4, id(arr4))

print('------------------------')
# shallow :- if you change val, it will reflect into 2nd copy as well
print('------------------------')

# add 2 into arr6 and check into arr7
arr3 = array([11, 12, 13, 14, 15])
arr4 = arr3.view()
arr3[1] = 111

# values are changing for both not one:
print(arr3, id(arr3))
print(arr4, id(arr4))




print('------------------------')
# deep copy :- use func copy: opp to shallow.
print('------------------------')

# add 2 into arr6 and check into arr7
arr3 = array([11, 12, 13, 14, 15])
arr4 = arr3.copy()
arr3[1] = 111

# values are changing for both not one:
print(arr3, id(arr3))
print(arr4, id(arr4))

