import math

for _ in range(int(input())):
    s = input()
    minDigit = math.inf
    i = 0

    while i < len(s):
        if s[i].isdigit():
            digit = 0
            # Process the entire sequence of digits
            while i < len(s) and s[i].isdigit():
                digit = digit * 10 + int(s[i])
                i += 1
            minDigit = min(digit, minDigit)
        else: i +=1

    print(minDigit)
