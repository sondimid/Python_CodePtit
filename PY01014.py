a,k,n = map(int,input().split())
check = False
for b in range(k-a%k,n-a+1,k):
    print(b, end = ' ')
    check = True
if check == False:
    print(-1)