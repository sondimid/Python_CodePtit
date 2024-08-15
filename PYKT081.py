import math
def check(a):
    if len(a) != 4: return "NO"
    for digit in a:
        if digit < 0 or digit > 255: return "NO"
    return "YES"
for _ in range(int(input())):
    a = list(map(int, input().split('.')))
    print(check(a))