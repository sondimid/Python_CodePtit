n = input()
a = []
for i in range(0, len(n) -1, 2):
    if n[i:i+2] not in a:
        a.append(n[i:i+2])
for i in a: print(i, end = ' ');