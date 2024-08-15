import math

for _ in range(int(input())):
    #line = input()
    s = input()
    t = input()
    start = 0
    cnt = 0
    while True:
        start = s.find(t, start )
        if start == -1:
            break
        cnt += 1
        start += len(t)
    print(cnt)