import math

while True:
    n = int(input())
    if n == 0: break
    a = []
    a.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
            a.append(n)
        else:
            n = n*3 +1
            a.append(n)
    print(len(set(a)))