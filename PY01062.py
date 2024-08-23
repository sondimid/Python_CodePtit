import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0: return False
    return n > 1
for _ in range(int(input())):
    n = input()
    cnt = 0
    for i in n:
        if isPrime(int(i)): cnt +=1
    if cnt > len(n) - cnt and isPrime(len(n)): print('YES')
    else: print('NO')
