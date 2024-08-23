import math
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)
    for i in a:
        if count.get(i) % 2 == 1:
            print(i)
            break