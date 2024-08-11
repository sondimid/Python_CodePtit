for t in range(int(input())):
    tmp = input()
    n,x,m = map(float,input().split()) 
    x /= 100.0
    i=0
    while n < m:
        i+=1
        n *=(1+x)
    print(i)