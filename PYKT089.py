n = int(input())
a = []
b = []
c = []
while len(c) < n:
    arr = list(map(int, input().split()))
    for i in arr:
        if i % 2 == 0: a.append(i)
        else: b.append(i)
        c.append(i)
i = 0
a.sort()
b.sort()
cnt1 = 0
cnt2 = len(b) - 1
for i in c:
    if i % 2 == 0:
        print(a[cnt1], end = ' ')
        cnt1 +=1
    else:
        print(b[cnt2], end = ' ')
        cnt2 -=1
