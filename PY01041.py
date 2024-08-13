import math
def find(s):
    if len(s) < 3: return -1
    for i in range(len(s)-1):
        if s[i] == s[i+1]: return -1
        if s[i] > s[i+1]: return i
    return -1
def check(s):
    i = find(s)
    if i == -1: return False
    for j in range(i,len(s)-1):
        if s[j] <= s[j+1]: return False
    return True
for t in range(int(input())):
    #line = input()
    s = input()
    if check(s): print('YES')
    else: print('NO')
