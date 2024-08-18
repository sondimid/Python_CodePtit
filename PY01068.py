res = []

def Try(i, pos):
    for j in range(pos,n):
        res[i] = a[j]
        if i == k-1:
            for idx in range(0,k):
                print(res[idx], end =' ')
            print()
        if i < k-1: Try(i+1,j+1)

n, k = map(int,input().split())
a = set(map(str, input().split()))
a = list(a)
n = len(a)
res = [0]*n
a.sort()
Try(0, 0)
