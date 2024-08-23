s = input()
a = []
for i in range(0,len(s)-1,2):
    a.append(int(s[i] + s[i+1]))
a = set(a)
a = list(a)
a.sort()
for i in a: print(i, end = ' ')
