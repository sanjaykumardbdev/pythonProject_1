# Fibonacci

a = 0
b = 1
c = 0
print(a)
print(b)
while c <= 10:
    c = a + b
    a = b
    b = c
    print(c)

# create triage

for i in range(5):
    print(i* "*")
    i=-1
print("------------")

for j in range(5):
    print(j* "*")
    j= j+1

print("------------")

j1 = 1
while j1 <= 5:
    print(j1 * "*")
    j1 = j1 + 1

print("---------------")
j1 = 5
while j1 <= 5:
    print(j1 * "*")
    j1 = j1 - 1
    if(j1 == 0):
        break

# =========================================
# in case of non numeric
print("fib ****************")
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    if n == 1:
        print(a)
        print(b)
    elif n < 0:
        print("invalid number")
    else:
        for i in range(2, n):
            c = a + b
            if c >= 50:
                break
            a = b
            b = c
            print(c)

fib(50)
