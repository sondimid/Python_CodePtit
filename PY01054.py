import math

for t in range(int(input())):
    #line = input()
    ans = 1
    s = input()
    for c in s:
        if(int(c) != 0):
            ans *= int(c)
    print(ans)