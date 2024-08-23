import math
a = []
for _ in range(int(input())):
    s = input()
    if s == '':
        print(a[0] + ':', len(a) - 1)
        a.clear()
    else: a.append(s)
print(a[0] + ':', len(a) - 1)
