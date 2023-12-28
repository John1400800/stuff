def r(n):
    #n>150
    hn = hex(n)[2:]
    hn = hn.replace('a', '1')
    e_cnt = 0
    for d in hn:
        if int(d, 16)%2==0: e_cnt += 1
    if e_cnt > 2:
        hn = hn + 'b'
    else:
        hn = 'f' + hn
    return int(hn, 16)

lst = []
for n in range(150, 170):
    if (res:=r(n))>3500:
        lst.append((n, res))

mn = min(lst, key=lambda tpl: tpl[1])[1]
print(min([tpl[0] for tpl in lst if tpl[1]==mn]))
    
