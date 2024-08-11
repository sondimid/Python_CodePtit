a,k,n = map(int,input().split())
check = False
for b in range(1,n-a+1):
    if (a+b) % k == 0: 
        print(b, end = ' ')
        check = True 
if check == False:
    print(-1)