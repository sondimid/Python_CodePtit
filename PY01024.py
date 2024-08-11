for t in range(int(input())):
    line = input()
    s = input()
    check = True
    sum=0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 10 != 0:
        check = False
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) != 2: check = False
    if check: print('YES')
    else: print('NO')
