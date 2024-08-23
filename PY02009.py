import math

for _ in range(int(input())):
    n = int(input())
    a = [0]*1005
    for i in range(n):
        a[int(input())] +=1
    ans = 0
    res = 0
    for i in range(1005):
        if a[i] > ans:
            ans = a[i]
            res = i
    print(res)