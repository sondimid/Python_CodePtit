import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return "NO"
    if n > 1 : return "YES"
    return "NO"
for t in range(int(input())):
    line = input()
    s = input()
    n = int(s[len(s)-4:])
    print(isPrime(n))