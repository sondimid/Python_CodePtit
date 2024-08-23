n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
a = list(a)
b = list(b)
a.sort()
b.sort()
check = True
if len(a) != len(b): check = False
for i in range(len(a)):
    if a[i] != b[i]:
        check = False
        break
if check: print('YES')
else : print('NO')