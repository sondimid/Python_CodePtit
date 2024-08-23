import math

for _ in range(int(input())):
    s = input()
    if len(s) <= 100: print(s)
    else:
        i = 99
        while s[i] != ' ': i -=1
        print(s[0:i])