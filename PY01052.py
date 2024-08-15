import math
def isPrime(n):
    if n < 2: return "NO"
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return "NO"
    return "YES"
for t in range(int(input())):
    #input()
    s = input()
    sum = 0
    for c in s:
        sum += int(c)
    print(isPrime(sum))