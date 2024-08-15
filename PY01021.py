import math

for _ in range(int(input())):
    s = input()
    t = ''
    digit = 0
    for c in s:
        if c.isdigit(): digit += int(c)
        else: t +=c
    t = ''.join(sorted(t))
    print(t+str(digit))