import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

def check(s):
    for i in range(len(s)):
        if isPrime(i) != isPrime(int(s[i])): return "NO"
    return "YES"

for t in range(int(input())):
    #line = input()
    s = input()
    print(check(s))