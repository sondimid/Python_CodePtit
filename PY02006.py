import math
def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]: return "NO"
    return "YES"
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(check(a,b))