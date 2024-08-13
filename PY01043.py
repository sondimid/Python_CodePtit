import math
nums = []
def check(s):
    for c in s:
        if int(c) % 2 == 1: return False
    return s == s[::-1] and len(s) % 2 == 0
def getNum(start, end):
    for i in range(start,end,2):
        if check(str(i)): nums.append(i)
getNum(10,100)
getNum(1000,10000)
getNum(100000,1000000)
for t in range(int(input())):
    #line = input()
    n = int(input())
    for i in nums:
        if i >= n: break
        print(i, end = ' ')
    print()


