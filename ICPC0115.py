import math
from math import factorial

for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += factorial(int(i))
    if sum == int(n): print('Yes')
    else: print('No')