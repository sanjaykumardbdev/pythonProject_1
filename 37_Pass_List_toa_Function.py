import numpy as np
from array import *


# count number of odd and even number from list
odd = 0
even = 0
def cnt_number(lst):
    for i in lst:
        if i % 2 == 0:
            globals()['even'] += 1
        else:
            globals()['odd'] += 1
    return odd, even


lst = [12, 13, 15, 16, 17, 23, 34, 45, 56, 45]
odd, even = cnt_number(lst)
print(odd, even)

print("even : {} odd: {}".format(odd, even))


# take 10 names from user and count user who have more then 5 letter
def chk_val():
    lst = array('i', [])
    n = int(input("Enter no. of name"))
    for i in range(n):
        inp = int(input("Enter number"))
        lst.append(inp)
        i+=1
    print(lst)

# chk_val()


def cnt_name():
    i = 0
    lst = np.array(['san', 'jay', 'ku', 'mar'])
    # print(lst[0])
    #print("len of lst", len(lst))
    for i in range(len(lst)):
        print(i)
        if len(lst[i]) >= 2:
            print(lst[i])
        else:
            return
        i+=1
cnt_name()

def tk_input():
    nm = np.array(['san'])
    for i in range(3):
        name = input("Enter name to store")
        np.append(nm, [name])
    print(name)
    for i in range(1):
        print(nm[i])

tk_input()
