for t in range(int(input())):
    #line = input()
    n = input()
    if int(n) % 7 == 0:
        print(n)
    else:
        cnt = 0
        check = False
        while(int(n) % 7 != 0 and cnt < 1000):
            n = str(int(n)+int(n[::-1]))
            cnt += 1
        if cnt == 1000:
            print(-1)
        else:
            print(n)
            
        