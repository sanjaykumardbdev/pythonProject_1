# Factorial using Recursion
def fact(n):
    if n == 0:
        return 1
    res = n * fact(n-1)
    return res

    #return n * fact(n-1)

result = fact(5)
print("fact of 5 ", result)

result = fact(10)
print("fact of 10 ", result)