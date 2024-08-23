import math

def check(s):
    t = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(t[i]) - ord(t[i-1])): return 'NO'
    return 'YES'
for _ in range(int(input())):
    print(check(input()))