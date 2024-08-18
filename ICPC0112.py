import math
prime = [1] * (10**6+5)
prime[0] = prime[1] = 0
for i in range(10**3+1):
    if prime[i] == 1:
        for j in range(i*i,10**6+1,i):
            prime[j] = 0
for _ in range(int(input())):
    ans = 0
    n = int(input())
    for i in range(n-6):
        if prime[i] == 1:
            if prime[i+6] == 1:
                if prime[i+2] == 1:
                    ans +=1
                if prime[i+4] == 1:
                    ans +=1
    print(ans)