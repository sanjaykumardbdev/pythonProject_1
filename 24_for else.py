nums = [24, 25, 30, 29, 59]

for i in nums:
    if i % 5 == 0:
        print(i)
        break
    # else will print multiple time as of if stmt
    # else:
# below else will print as part of for loop
else:
    print("not found")
