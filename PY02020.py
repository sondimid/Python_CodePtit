n = int(input())
a = list(map(float, input().split()))
m = min(a)
M = max(a)
size = 0
s = 0
for i in a:
    if i != m and i != M:
        s += i
        size +=1
ans = round(s / size, 2)
print(ans)
