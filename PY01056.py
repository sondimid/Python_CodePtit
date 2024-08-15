import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n >1
def check(s):
    sum = 0
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2: return False
        sum +=int(s[i])
    return isPrime(sum)
for t in range(int(input())):
    line = input()
    s = input()
    if check(s): print("YES")
    else: print("NO ")