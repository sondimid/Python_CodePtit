import math
def isPrime(n):
    if n==0 or n==1: return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True 
for t in range(int(input())):
    n = int(input())
    k=0
    for i in range(1,n):
        if math.gcd(n,i) == 1:
            k += 1
    if isPrime(k):
        print('YES')
    else: print('NO')
    