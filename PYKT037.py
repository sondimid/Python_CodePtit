def convert(n, b):
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    while n > 0:
        remainder = n % b
        ans += digit[remainder]
        n //= b
    return ans[::-1]


import math

for t in range(int(input())):
    #line = input()
    n, b = map(int,input().split())
    print(convert(n,b))