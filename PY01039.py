def check(s):
    if len(set(s)) != 2: return False
    for i in range(len(s)-2):
        if s[i] != s[i+2]: return False
    return True
for t in range(int(input())):
    line = input()
    s = input()
    if check(s): print('YES')
    else: print('NO')