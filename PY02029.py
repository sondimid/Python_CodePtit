from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
count = Counter(a)
M = count.most_common()[0]

ans = 0
res = 0
for i in a:
    if M[1] > count.get(i) > res:
        ans = i
        res =  count.get(i)
if ans != 0: print(ans)
else: print('NONE')
