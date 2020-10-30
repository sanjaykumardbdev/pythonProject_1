#  Anonymous Functions
def square(a):
    return a * a
result = square(5)
print(result)

print("-----------------------")

f = lambda a: a*a
result = f(5)
print(result)

print("-----------------------")
# lambda should be in one expression:
f = lambda a,b: a +b
result = f(5,6)
print(result)
