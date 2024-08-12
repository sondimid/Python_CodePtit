import math
for t in range(int(input())):
    line = input()
    n,x,m = map(float,input().split()) 
    x /= 100.0
    print(math.ceil(math.log(m/n,1+x)))