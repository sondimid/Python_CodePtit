for t in range(int(input())):
    line = input()
    s = input()
    if s[0] == s[len(s)-1] and s[1] == s[len(s)-2]: print('YES')
    else: print('NO')