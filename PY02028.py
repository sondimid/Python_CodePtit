isPrime = [1] * 1005
isPrime[0] = isPrime[1] = 0
prime = []
for i in range(1005):
    if isPrime[i] == 1:
        for j in range(i * i, 1005, i):
            isPrime[j] = 0
n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    if isPrime[i] == 1: prime.append(i)
prime.sort()
for i in range(len(a)):
    if isPrime[a[i]] == 1:
        print(prime[cnt], end = ' ')
        cnt +=1
    else: print(a[i], end = ' ')
