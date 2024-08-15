def check(a, n):
    for i in range(2,n+1):
        if a % i == 0: return False
    return True
while True:
    num = list(map(int, input().split()))
    #input()
    if num[0] == -1: break
    l = num[0]
    r = num[1]
    n = int(input())
    #input()
    cnt = 0
    for i in range(l, r+1):
        if check(i, n): cnt +=1
    print(cnt)