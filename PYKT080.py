import math

n, m = map(int, input().split())
a = [[0]]*n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

cnt = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                newDx = i + dx[k]
                newDy = j + dy[k]
                if 0 <= newDx and newDx < n and newDy >= 0 and newDy < m :
                    if a[newDx][newDy] != 0:
                        cnt += a[newDx][newDy]
                        a[newDx][newDy] = 0
print(cnt)
