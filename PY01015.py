def check(s):
    for i in range(1,len(s)):
        if s[i] < s[i-1]: return False
    return True
for t in range(int(input())):
    line = input()
    s = input()
    if check(s): print('YES')
    else: print('NO')