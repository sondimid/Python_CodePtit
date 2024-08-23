from collections import Counter

s = input()
a = []
for i in range(0,len(s)-1,2):
        a.append(int(s[i] + s[i+1]))
count = Counter(a)
b = []
for i in a:
    if i not in b:
        print(i, count.get(i))
        b.append(i)
