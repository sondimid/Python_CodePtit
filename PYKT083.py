import math
price = {
    ("Xe_con", 5): 10000,
    ("Xe_con", 7): 15000,
    ("Xe_tai", 2): 20000,
    ("Xe_khach", 29):50000,
    ("Xe_khach", 45): 70000
}
daily_fee = {}
for _ in range(int(input())):
    s = input().split()
    type = s[1]
    num = int(s[2])
    d = s[3]
    date = s[4]
    if d == "IN":
        fee = price.get((type, num))
        if date in daily_fee:
            daily_fee[date] +=fee
        else: daily_fee[date] = fee
for date, fee in daily_fee.items():
    print(f'{date}: {fee}')