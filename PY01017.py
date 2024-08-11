for t in range(int(input())):
    line = input()
    s = input()
    i = 0
    while i < len(s):
        cnt = 1
        while i < len(s)-1 and s[i] == s[i+1]:
            cnt += 1
            i += 1
        print(cnt,end = '')
        print(s[i],end = '')
        i += 1