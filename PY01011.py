def check(n):
    s = str(n)
    t = s[::-1]
    if s != t: return False
    for c in s:
        if int(c) % 2 != 0: return False
    if(len(s) % 2 != 0): return False
    return True
for t in range(int(input())):
    line = input()
    n = int(input())
    for i in range(n):
        if check(i): print(i, end=' ')