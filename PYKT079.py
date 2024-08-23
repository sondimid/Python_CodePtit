import math

for _ in range(int(input())):
    n = int(input())
    se = list(map(int, input().split()))
    se = set(se)
    m = min(se)
    M = max(se)
    print(M-m +1 -len(se))