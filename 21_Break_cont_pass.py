for i in range(1, 5):
    if i == 3:      # will break this loop once i = 3
        break
    print("hello", i)

print("------------")
for i in range(5):
    if i == 3:      # will not print value of i, it it is 3. it will pass/skip value of i when it is 3
        pass
    print("hello", i)

# example


def fun():
    pass


class TEST:
    pass
