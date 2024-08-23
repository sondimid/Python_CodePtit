while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    m = min(a)
    M = max(a)
    if m == M: print('BANG NHAU')
    else: print(f'{m} {M}')