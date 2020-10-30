from array import *

# Factorial
# 5! = 5 * 4 * 3 * 2 * 1

def facto(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        # print(i, f)
    return f

result = facto(5)
print(result)
