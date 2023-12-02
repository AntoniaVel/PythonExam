import random


lst = [random.randint(1, 5) for x in range(10)]
print(lst)

flag = 0

for i in range(len(lst)):
    if lst[i] == 2:
        print(i)
        flag = 1
        break

if flag != 1:
    print(len(lst))
