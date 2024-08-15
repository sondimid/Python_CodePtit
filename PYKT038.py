import math


def convert(s):
    ans = ""
    t = ""
    for i in range(0,len(s)):
        t += s[i]
        if i % 3 == 2:
            digit = 0
            t = t[::-1]
            for j in range(len(t)):
                digit += int(t[j]) * int(math.pow(2,j))
            ans += str(digit)
            t =""
    return ans

n = input()
n = '0'*(3 - len(n) % 3) + n
print(convert(n))