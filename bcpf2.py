num = 0
for i in range(10):
    userIn = int(input("in: "))
    if(userIn < 0):
        continue
    num += userIn
print(num)