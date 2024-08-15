s1 = list(map(str, input().split()))
s2 = input()
p = int(input())
p -=1
for i in range(len(s1)):
    if i == p: print(s2, end = '')
    print(s1[i], end = ' ')


