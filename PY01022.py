n = input()
cnt = 0
if len(n) == 1: print(1)
else:
    while len(n) != 1:
        digit = 0
        for c in n:
            digit += int(c)
        n = str(digit)
        cnt += 1
    print(cnt)