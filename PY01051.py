import math
def check(n):
    sum = 0
    for i in n:
        sum += int(i)
    return str(sum) == str(sum)[::-1] and len(str(sum)) > 1
for t in range(int(input())):
    #line = input()
    n = input()
    if check(n): print('YES')
    else: print('NO')
