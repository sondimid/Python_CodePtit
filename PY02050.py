import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [1] * n
    stack = []
    for i in range(n):
        if len(stack) == 0: stack.append(i)
        else:
            while len(stack) > 0 and a[stack[-1]] <= a[i]:
                stack.pop()
            if len(stack) > 0: b[i] = i - stack[-1]
            else: b[i] = i + 1
            stack.append(i)
    for i in b: print(i, end = ' ')
    print()
