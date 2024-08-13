import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1
def check(s):
    cnt = 0
    for c in s:
        if isPrime(int(c)): cnt +=1
    return cnt > len(s) - cnt and isPrime(len(s))
for t in range(int(input())):
    #line = input()
    s = input()
    if check(s): print('YES')
    else: print('NO')