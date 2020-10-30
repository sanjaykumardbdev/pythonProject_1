# keyworded variable length arguments

def person(name,*data):
    print(name)
    print(data)

person('san', 28, 'bangalore', 98989898)

# ** means, you are passing keyword with data
def person1(name,**data):
    print(name)
    # print(data)
    for i in data:
        print(i, end=" ")
        print(data[i], end=" ")

    print()
    print("-------------")

    for i, j in data.items():
        print(i, ":-", j)

person1('san', age =28, city = 'bangalore', mob= 98989898)

person1('san', age =20, city = 'bangalore', mob= 1111111)