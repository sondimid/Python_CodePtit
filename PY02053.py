n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i + j < n-1: sum1 +=a[i][j]
        elif i + j > n -1: sum2 +=a[i][j]
k = int(input())
if abs(sum1 - sum2) <= k:print("YES")
else : print("NO")
print(abs(sum1 - sum2))