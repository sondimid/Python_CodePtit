while True:
    line = input()
    if line == "0 0 0 0": break
    a = list(map(int,line.split()))
    cnt = 0
    while True:
        if a[0] == a[1] and a[1] == a[2] and a[3] == a[2] and a[3] == a[0]: break
        for i in range(3):
            a[i] = abs(a[i] - a[i+1])
        a[3] = abs(a[3]-a[0])
        cnt +=1
    print(cnt)