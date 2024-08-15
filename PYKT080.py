import math

n, m = map(int, input().split())
a = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

cnt = 0
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                newDx = i + dx[k]
                newDy = j + dy[k]
                if newDx >=0 and newDy >=0 and newDx < n and newDy < m and a[newDx][newDy] >=0: cnt +=a[newDx][newDy]
print(cnt)
