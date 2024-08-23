isPrime = [1] * 100000
prime = []
isPrime[0] = isPrime[1] = 0
for i in range(10000):
    if isPrime[i]:
        for j in range(i*i, 100000, i):
            isPrime[j] = 0
        prime.append(i)
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    num = 10**6
    for j in prime:
        num = min(num, abs(i - j))
    ans = max(ans, num)
print(ans)
