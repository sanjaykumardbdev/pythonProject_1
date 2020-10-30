# type of argument

def add(a, b):  # formal arg
    c = a + b
    print(c)


add(10, 20)  # actual arg 1: position, keywork, default, variable length


def person(name, age):
    print(name)
    print(age-2)

person('sanjay',34)                 # position
person(age= 28, name = 'sanjay')    # keyword

def person(name, age= 18):
    print(name)
    print(age-2)
person('sanjay')                 # default

print("============================== variable len char")
def sum(a, *b):  # formal arg
    c = 0
    print(a, b)
    for i in b:
        c = c + i
    c = c + a
    print(c)

sum(2)
sum(2, 2, 3, 3)

