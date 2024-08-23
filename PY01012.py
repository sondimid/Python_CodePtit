s1 = input()
s2 = input()
p = int(input())
p -=1
res = s1[:p] + s2 + s1[p:]
print(res)