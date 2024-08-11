p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    k,s = input().split()
    k = int(k)
    if k == 0: break
    t = ''
    for i in range(len(s)):
        idx = (ord(s[i]) - ord('A') + k) % 28
        t += p[idx]
    print(t[::-1])
    line = input()
    