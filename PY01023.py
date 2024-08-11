import math
for t in range(int(input())):
    line = input()
    n = int(input())
    print(1,end = ' ')
    for i in range(2,int(math.sqrt(n))+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            print('*', end = ' ')
            print(i, end = '')
            print('^', end = '')
            print(cnt, end = ' ')
    if n != 1: 
        print('*', end = ' ')
        print(int(n), end = '')
        print('^',end = '')
        print(1)
    else: print()