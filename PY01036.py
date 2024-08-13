for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(2 -  n%2,n+1,2):
        ans += float(1/i)
    print(f"{ans:.6f}")