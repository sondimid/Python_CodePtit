n = int(input())
a = []
for i in range(n):
    row = input()
    a.append(row)
ans = 0
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if a[i][j] == 'C': cnt1 +=1
        if a[j][i] =='C': cnt2 +=1
    ans += cnt1*(cnt1-1)/2 + cnt2*(cnt2-1)/2;
print(int(ans))