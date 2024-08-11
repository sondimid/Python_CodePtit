a = list(int(i) for i in input())
k=0
for i in a:
    if i==4 or i==7: k+=1
if k==4 or k==7: print('YES')
else: print('NO')