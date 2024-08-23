import math
from collections import Counter


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if isPrime(i):
        print(f'{i} {Counter(a)[i]}')
        for j in range(len(a)):
            if a[j] == i: a[j] = 0

