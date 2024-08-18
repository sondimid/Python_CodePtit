t = int(input())
for i in range(t) :
    n, m = [x for x in input().split()]
    n = min(n,m)
    m = max(n,m)
    a = input().strip()
    if(a.count(' ')) : a, b = a.split()
    else : b = input()
    print(int(a.replace(m,n)) + int(b.replace(m,n)), end = ' ')
    print(int(a.replace(n,m)) + int(b.replace(n,m)))
