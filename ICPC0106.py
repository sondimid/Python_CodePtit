import math
so = ['A','B','C','D','E','F']
def convert(s, b):
    ans = ""
    tmp = ""
    for i in range(len(s)):
        tmp += s[i]
        if i % b == b-1:
            digit = 0
            tmp = tmp[::-1]
            for j in range(len(tmp)):
                digit += int(tmp[j])*(2**j)
            tmp = ""
            if digit >= 10: ans += so[digit % 10]
            else :ans += str(digit)
    return ans
for _ in range(int(input())):
    b = int(input())
    b = int(math.log(b,2))
    s = input()
    s = '0'*(b - len(s) % b) + s
    ans = convert(s, b)
    for i in range(len(ans)):
        if i == 0 and ans[i] == '0': continue
        print(ans[i],end='')
    print()
