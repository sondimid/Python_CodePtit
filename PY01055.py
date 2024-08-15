import math
def check(s):
    if len(s) % 2 == 0: return "NO"
    if s[0] == [1]: return "N0"
    for i in range(0,len(s)-2,2):
        if s[i] != s[i+2]: return "NO"
    if s[0] != s[len(s)-1]: return "NO"
    return "YES"
for t in range(int(input())):
    #line = input()
    s = input()
    print(check(s))
    
