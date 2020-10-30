from array import *

arr = array('i', [])

n = int(input("Enter length of arr"))
for i in range(n):
    x = int(input("Enther next val of arr"))
    arr.append(x)

# print(arr)
for i in arr:
    print(i)

k = 0
search = int(input("Enter val to search"))
for e in arr:
    if e == search:
        print('for loop', k)
        break
    k =+ 1

print("index of search ele", arr.index(search))

# using while loop
k = 0
print("len of arr", len(arr))

i = 0
search1 = int(input("Enter val to search using while loop"))
while i <= len(arr):
    if arr[i] == search1:
        print("index of search ele", arr.index(search1))
        print("value of search ", arr[i])
        break
    i += 1
