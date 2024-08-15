s = input()
i = 0
ans = 'YES'
while i < len(s):
    if s[i] == '6':
        if i + 1 < len(s) and s[i+1] == '8':
            if i + 2 < len(s) and s[i+2] == '8':
                i +=3
            else: i +=2
        else: i+=1
    else:
        ans = 'NO'
        break
print(ans)