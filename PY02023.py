import math
from functools import cmp_to_key
def cmp(s, t):
    sum = 0
    sum1 = 0
    for i in s: sum += int(i)
    for i in t: sum1 += int(i)
    if sum == sum1:
        if int(s) > int(t): return 1
        else: return -1

    elif sum > sum1: return 1
    else: return -1
for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    a = sorted(a, key=cmp_to_key(cmp))
    print(' '.join(a))
