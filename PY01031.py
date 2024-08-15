import math
sample = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert(n, b):
    res = ''
    while n > 0:
        remainder = n % b
        res += sample[remainder]
        n //= b
    return res[::-1]
for _ in range(int(input())):
    n, b = map(int,input().split())
    print(convert(n, b))
