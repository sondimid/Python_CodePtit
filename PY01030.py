import math
n,k = map(int,input().split())
cnt=0
for m in range(10**(k-1),10**k):
    if math.gcd(n,m) == 1:
        print(m,end=' ')
        cnt += 1 
        if cnt == 10: 
            print()
            cnt = 0