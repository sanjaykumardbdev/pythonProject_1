x = int(input("how many candies you want"))
i = 1
av = 5
while i <= x:
    if i > av:
        print("out of stock")
        break
    print(i, "Candy")
    i += 1

# print number which is not divisible by neither 3 nor 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
print("bye")

# print only even number between range of 1 to 101
for i in range(1, 101):
    if i % 2 == 0:
        pass
    else:
        print(i)
print("bye")