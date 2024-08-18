import math

for _ in range(int(input())):
    n , d = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(0,n):
        print(a[(i + d) % n], end = ' ')
    print()

