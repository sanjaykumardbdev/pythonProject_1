def div(a, b):
    if(a < b):
        a = a + b
        b = a - b
        a = a - b
        print(a / b)
    else:
        print(a/b)

div(14, 7)
div(7, 14)

print("-----------------------------------")
def div1(a, b):
    if(a < b):
        a,b = b,a
    print(a/b)

div1(14, 7)
div1(7, 14)

print("---------------------decorators--------------")
# change the behabior of existing function at compile time:
# func within func:
# python is functional programming:
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div = div(2,4)
