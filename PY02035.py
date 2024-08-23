from collections import Counter

s = input()
k = int(input())
a = []
for i in range(0, len(s)-1, 2):
    a.append(s[i] + s[i+1])
count = Counter(a)
a.sort()
check = False
b = []
for i in a:
    if i not in b and count.get(i) >= k:
        print(i, count.get(i))
        check = True
        b.append(i)
if not check: print('NOT FOUND')