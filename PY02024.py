import math
from functools import cmp_to_key
def cmp(s1 , s2):
    mul1 = 1
    mul2 = 1
    for i in s1: mul1 *= int(i)
    for i in s2: mul2 *= int(i)
    if mul1 == mul2:
        if int(s1) > int(s2): return 1
        else: return -1
    elif mul1 > mul2: return 1
    return -1
for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    a = sorted(a,key = cmp_to_key(cmp))
    print(' '.join(a))