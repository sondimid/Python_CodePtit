import math

n = int(input())
a = list(map(int, input().split()))
step = 1000000
ans = 0
for i in a:
    x = 0
    for j in a:
        x += abs(i - j)
    if step > x:
        ans = i
        step = x
print(step, ans)