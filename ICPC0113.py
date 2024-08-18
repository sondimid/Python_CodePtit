import math
prime = [1]*(10**6+5)
prime[0] = prime[1] = 0
for i in range(1005):
    if prime[i] == 1:
        for j in range(i*i, 10**6,i):
            prime[j] = 0
def check(n, s):
    if prime[int(n)] == 1 and prime[int(n[::-1])] == 1 and n != n[::-1]  and int(s) > int(n[::-1]): return True
    return False
for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        if check(str(i), n):
            s = str(i)
            s = s[::-1]
            if i not in a and int(s) not in a:
                a.append(i)
                a.append(int(s))
    for i in a: print(i, end = ' ')
    print()

