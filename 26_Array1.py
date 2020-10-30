from array import *
import array as arr



# values = arr.array('I', [1, 2, 3, -4, 5])

values = arr.array('i', [1, 2, 3, -4, 5])

print(values.buffer_info())
print(values.reverse())
print(values)

for i in range(5):
    print(values[i])

for i in range(len(values)):
    print(values[i])

for e in values:
    print(e)

# ----------------
# work with char
print('-------------')

char_values = arr.array('u', ['a', 'i', 'u'])

for e in char_values:
    print(e)

print('-------------')
values1 = arr.array('i', [2, 3, 4, 5, 6])
newArr = array(values1.typecode, (a*a for a in values1))
# newArr = array(values1.typecode, (math.sqrt(a) for a in values1))
for e in newArr:
    print(e)

print('------------- using while loop')
i =0
while i < len(newArr):
    print(newArr[i])
    i += 1
