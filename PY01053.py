import math

for t in range(int(input())):
    input()
    s = input()
    sum = 0
    for c in s:
        sum += int(c)
    if sum % 3 == 0: print("YES")
    else: print("NO")