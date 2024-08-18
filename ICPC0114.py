import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    sum = 0
    for i in n:
        sum +=int(i)
        if not isPrime(int(i)): return 'No'
    if isPrime(int(n)) and isPrime(sum) and isPrime(int(n[::-1])): return 'Yes'
    return 'No'
for _ in range(int(input())):
    n = input()
    print(check(n))

