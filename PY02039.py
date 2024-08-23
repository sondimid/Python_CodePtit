n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(n):
        if i > j: s1 += a[i][j]
        elif i < j: s2 += a[i][j]
if abs(s1 - s2) <= k: print("YES")
else: print("NO")
print(abs(s2 - s1))