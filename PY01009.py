s = input()
cnt = 0
for c in s:
    if c.islower(): cnt+=1
if cnt >= len(s)-cnt: print(s.lower())
else: print(s.upper())