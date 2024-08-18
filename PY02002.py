import math
fibo = [0]*100
fibo[1] = fibo[2] = 1
for i in range(3,93):
    fibo[i] = fibo[i-1] + fibo[i-2]
for _ in range(int(input())):
    a, b = map(int,input().split())
    for i in range(a, b+1):
        print(fibo[i], end = ' ')
    print()