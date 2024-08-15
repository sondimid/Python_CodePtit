import math
t = int(input())
for i in range(t):
    #input()
    a = int(input())
    #input()
    b = input()
    ans = 0
    for c in b:
        ans = (ans * 10 + int(c)) % a
    print(math.gcd(a, ans))
