import math
def check(s):
    for c in s:
        if c != '0' and c != '1' and c != '2':
            return "NO"
    return "YES"
for t in range(int(input())):
    #line = input()
    s = input()
    print(check(s))
