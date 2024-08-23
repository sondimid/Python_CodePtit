import math

for _ in range(int(input())):
    n,m,l = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    i = j = k = 0
    check = False
    while i < n and j < m and k < l:
        if a[i] == b[j] and a[i] == c[k]:
            print(a[i], end = ' ')
            i +=1
            j +=1
            k +=1
            check = True
        elif a[i] <  b[j]:
            i +=1
        elif b[j] <  c[k]:
            j +=1
        else: k +=1
    if not check: print('NO')
    else: print()
