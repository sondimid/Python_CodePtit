n = input()
s = n[::-1]
res=''
cnt=0
for i in s:
    
    if cnt == 3:
        cnt = 0
        res += ','
    res += i
    cnt += 1
print(res[::-1])
    