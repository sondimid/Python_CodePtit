import math
for t in range(int(input())):
    #line = input()
    n = input()
    m = int(n[::-1])
    n = int(n)
    if math.gcd(n,m) == 1:
        print('YES')
    else: print('NO')