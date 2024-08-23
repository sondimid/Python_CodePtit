n = int(input())
a = set(map(int, input().split()))
a = list(a)
check = False
for i in range(len(a) - 1):
    if a[i+1] - a[i] != 1:
        print(a[i] + 1)
        check = True
        break
if not check: print(a[len(a)-1] + 1)