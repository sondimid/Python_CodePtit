n = 0
k = 0
arr = []
se = set()
a = []
def Try(i,pos):
    for j in range(pos,n+1):
        arr[i-1] = a[j-1]
        if i == k:
            for l in range(i):
                print(arr[l], end = ' ')
            print()
        elif i < k: Try(i+1,j+1)


n, k = map(int,input().split())
#input()
se = set(map(int,input().split()))
n = len(se)

a = sorted(list(se))
arr = [0] * k
Try(1,1)
