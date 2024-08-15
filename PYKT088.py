import math

n = int(input())
ans = 0
for m in range(1,n+1):
    cnt = 0
    for i in range(1,int(math.sqrt(m))+1):
        if m % i == 0:
            cnt +=1
            if m/i != i: cnt +=1
    if cnt == 9: ans +=1
print(ans)
