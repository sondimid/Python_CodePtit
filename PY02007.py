a = []
size = 0
while True:
    b = list(map(int, input().split()))
    size += len(b)
    for i in b: a.append(i)
    if size == 10: break

for i in range(len(a)):
    a[i] %= 42
print(len(set(a)))