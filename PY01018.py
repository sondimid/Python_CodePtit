p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    inp = input()
    if inp[0] == '0': break
    k,s = inp.split()
    k = int(k)
    t = ''
    for i in range(len(s)):
        idx = (p.find(s[i]) + k) % 28
        t += p[idx]
    print(t[::-1])
    