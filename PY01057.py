import math
def isPrime(n):
    return n == 2 or n == 3 or n == 5 or n == 7

def check(s):
    for i in range(len(s)):
        if isPrime(i) != isPrime(int(s[i])): return "NO"
    return "YES"

for t in range(int(input())):
    line = input()
    s = input()
    print(check(s))