import math


def round_score(score):

    rounded_score = round(score,2)

    if rounded_score - int(rounded_score) == 0.25:
        return rounded_score + 0.25
    elif rounded_score - int(rounded_score) == 0.75:
        return rounded_score + 0.25
    else:
        return float(int(rounded_score))
for _ in range(int(input())):
    r, l, s, w = map(str,input().split())
    r = int(r)
    s = float(s)
    w = float(w)
    if r >= 39: r = 9.0
    elif r >= 37: r = 8.5
    elif r >= 35: r = 8.0
    elif r >= 33: r = 7.5
    elif r >= 30: r = 7.0
    elif r >= 27: r = 6.5
    elif r >= 23: r = 6.0
    elif r >= 20: r = 5.5
    elif r >= 16: r = 5.0
    elif r >= 13: r = 4.5
    elif r >= 10: r = 4.0
    elif r >= 7: r = 3.5
    elif r >= 5: r = 3.0
    elif r >= 3: r = 2.5
    l = int(l)
    if l >= 39: l = 9.0
    elif l >= 37: l = 8.5
    elif l >= 35: l = 8.0
    elif l >= 33: l = 7.5
    elif l >= 30: l = 7.0
    elif l >= 27: l = 6.5
    elif l >= 23: l = 6.0
    elif l >= 20: l = 5.5
    elif l >= 16: l = 5.0
    elif l >= 13: l = 4.5
    elif l >= 10: l = 4.0
    elif l >= 7: l = 3.5
    elif l >= 5: l = 3.0
    elif l >= 3: l = 2.5
    score = (l + r + s + w) /4
    print(round_score(score))

