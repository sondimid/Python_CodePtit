import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
for t in range(int(input())):
    line = input()
    a,b = map(int,input().split())
    sum = 0
    s = str(math.gcd(a,b))
    for c in s:
        sum += int(c)
    if isPrime(sum): print('YES')
    else: print('NO')
    
        