from numpy import *

print("normal array ---------------")
# arr = array([23, 23, 23, 23, 23], int)
arr = array([23, 23, 23, 23, 23], float)
print(arr)
print(arr.dtype)

print("linspace --------------- gap bet 2 ele will be same")
# arr1 = linspace(0, 15, 16)
# arr1 = linspace(0, 15, 20)
# by default it will divide into 15 parts
# arr1 = linspace(0, 15, 2)
arr1 = linspace(0, 15)
print(arr1)

print("logspace --------------- spacing btw 2 num depending on log"
      "so it will be divided into 5 parts"
      "it will start from 10 ways to 1 till 10 ways to 40")

arr_logspace = logspace(1, 40, 5)
print(arr_logspace)
print(arr_logspace[0])      # 10 isto 1
print(arr_logspace[4])      # 10 isto 40

print('%.2f' %arr_logspace[0])
print('%.2f' %arr_logspace[4])
print(len('10000000000000000303786028427003666890752'))

# arr_z = zeros(5, int)
arr_z = ones(5, int)
print(arr_z)

