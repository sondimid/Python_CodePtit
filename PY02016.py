import math
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans, frequent = Counter(a).most_common()[0]
    if frequent > n /2: print(ans)
    else: print("NO")