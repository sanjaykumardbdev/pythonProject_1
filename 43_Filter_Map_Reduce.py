from functools import reduce
# Filter Map Reduce
def is_even(n):
    return n%2==0
def update(n):
    return n*n
def add_all(a,b):
    return a+b

nums = [3, 2, 4, 5, 6, 7, 8, 9, 45, 6]
evens = list(filter(is_even, nums))
print(evens)
doubs = list(map(update,evens))
print(doubs)
sum = reduce(add_all,doubs)
print(sum)



# --------------------------------------------
print(" --------------------------------------------")

nums = [3, 2, 4, 5, 6, 7, 8, 9, 45, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
doub = list(map(lambda n: n * n, evens))
sum = reduce(lambda a,b : a+b,doub)

print(evens)
print(doub)
print(sum)