import math

for _ in range(int(input())):
    n = input()
    sum = 0
    mul = 1
    check = False
    for i in range(len(n)):
        if i % 2 == 0: sum +=int(n[i])
        if i % 2 == 1:
            if int(n[i]) != 0:
                check = True
                mul *= int(n[i])
    if not check: mul = 0
    print(f'{sum} {mul}')

