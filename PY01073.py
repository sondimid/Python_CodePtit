import itertools

per = itertools.permutations(input())
for p in per:
    for c in p:
        print(c,end = '')
    print()