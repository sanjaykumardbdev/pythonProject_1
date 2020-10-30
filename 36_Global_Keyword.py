# global variable
a = 10
print("global id", id(a))
b = 34
def test():
    a = 14
    x = globals()['a']
    print("inside test", id(x))
    print("in func", a)
    print("val of x", x)        # access global val which is same as local var.
    y = globals()['a'] = 23
    print(y)

print("in global- outside test", a)
test()
