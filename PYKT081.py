import math
def check(a):
    if len(a) != 4: return "NO"
    for digit in a:
        if digit.isdigit():
            if int(digit) < 0 or int(digit) > 255: return "NO"
        else: return "NO"
    return "YES"
for _ in range(int(input())):
    a = input().split('.')
    # print(a)
    print(check(a))