n = int(input())
a = []
ans = []
quantity = 0
for i in range(n):
    s = input().split()
    a.append(s)
i = 0
while i < len(a):
    if len(a[i]) == 7:
        quantity +=1
        ans.append(2)
        i +=4
    else:
        while i < len(a) and len(a[i]) != 7:
            i +=1
        ans.append(1)
        quantity +=1
print(quantity)
for i in ans: print(i)
