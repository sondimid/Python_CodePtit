import math



for _ in range(int(input())):
    s = input()
    maxDigit = -1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            digit = 0
            while i < len(s) and s[i].isdigit():
                digit = digit*10 + int(s[i])
                i +=1
            maxDigit = max(digit, maxDigit)
        else: i +=1
    print(maxDigit)