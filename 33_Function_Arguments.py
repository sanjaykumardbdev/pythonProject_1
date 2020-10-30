# pass by val/ref

def update(x):
    x = 8
    print(x)

update(10)

def update1(x):
    x = 8
    print(x)
a = 10
update1(a)
print("a ", a)


# pass by value/reference

def update1(x):
    print(id(x))
    x = 8
    print("newid", id(x))
    print(x)
a = 10
print(id(a))
update1(a)
print("a ", a)


def update1(lst):
    print(id(lst))
    lst[1] = 25
    print("newid", id(lst))
    print("x ", lst)

lst = [10, 20, 30]
print(id(lst))
update1(lst)
print("lst ", lst)

