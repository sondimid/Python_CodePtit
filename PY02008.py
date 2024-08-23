isPrime = [1]* (10**4)
isPrime[0] = isPrime[1] = 0
for i in range(2, 100):
    if isPrime[i] == 1:
        for j in range(i*i, 10**4, i):
            isPrime[j] = 0
prime = []
for i in range(10**4):
    if isPrime[i] == 1: prime.append(i)

n, x = map(int,input().split())
print(x, end = " ")

for i in range(n):
    x +=prime[i]
    print(x, end = " ")