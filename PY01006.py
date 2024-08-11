for t in range(int(input())):
    a = list(int(i) for i in input())
    check = True
    for i in a:
        if i != 4 and i != 7: check = False
    if check == True: print('YES')
    else: print('NO')
    