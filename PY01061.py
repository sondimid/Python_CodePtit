import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

for _ in range(int(input())):
    n = input()
    if isPrime(int(n[0:3])) and isPrime(int(n[-3:])): print('YES')
    else: print('NO')
