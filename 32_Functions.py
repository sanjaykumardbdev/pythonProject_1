# define a function
# call a function
def greet():
    print("first function in python")
    print("Hello ! Good Morning")

greet()
print("-----------")

# pass 2 arguments
def add(x,y):
    z = x + y
    print("sum of two num", z)

add(3,3)
add(12, 12)

# function that return value
def add_return(x, y):
    z = x + y
    return z
# return val is stored in ret_val :
ret_val = add_return(3, 3)
print("function that return value", ret_val)

# return 2 values
def add_sub(x, y):
    a = x + y
    b = x - y
    return a, b

add1, sub1 = add_sub (20, 10)
print('add1 ->', add1, "sub1 ->", sub1)

