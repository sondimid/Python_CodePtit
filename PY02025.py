

n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
a = list(a)
b = list(b)
a.sort()
b.sort()
i = j = 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        print(a[i], end =' ')
        i +=1
        j +=1
    elif a[i] > b[j]: j +=1
    else: i +=1
print()
for num in a:
    if num not in b: print(num, end = ' ')
print()
for num in b:
    if num not in a: print(num, end = ' ')
