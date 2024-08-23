

isPrime = [1] * 10**6
isPrime[0] = isPrime[1] = 0
for i in range(10**3):
    if isPrime[i]:
        for j in range(i*i, 10**6, i):
            isPrime[j] = 0
n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b: b.append(i)
l = 0
r = sum(b)
check = False
for i in range(len(b)):
    l += b[i]
    r -= b[i]
    if isPrime[l] and isPrime[r]:
        print(i)
        check = True
        break
if not check: print('NOT FOUND')

