import csv


def conv(s):
    return s[0], int(s[1])


def by_price(s):
    return s[1]


enc = 'utf-8'
sum = 1000

with open('wares.csv', encoding=enc) as csv_f:
    readr = csv.reader(csv_f, delimiter=';')
    tbl = map(conv, readr)
    res = []
    for n, p in sorted(tbl, key=by_price):
        cnt = sum // p
        if cnt > 10:
            cnt = 10
        if cnt != 0:
            res.extend([n] * cnt)
        sum -= p * cnt
    if res:
        print(*res, sep=', ')
    else:
        print('error')