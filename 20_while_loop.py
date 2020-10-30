i=1
while i<=5:
    print( "Hello")
    i+=1





i=1
while i<=5:
    print( i, "Hello")
    i = i + 1


print("-----------")
j=5
while j>=1:
    print( j, "Hello")
    j = j - 1

print("-----------")

j = 5
i = 4
while j >= 1:
    print(j, "Hello")
    while i >= 1:
        print(i, "hi")
        i = i - 1
    j = j - 1

print("-----------")


j=5
while j>=1:
    print( j, "Hello ",end="")
    i = 4
    while i>=1:
        print(i,"Hi ",end="")
        i = i - 1
    j = j - 1
    print()
