from itertools import permutations


alpha='ярослав'
vow = 'яоа'
cons = 'рслв'
def valid_(w):
    v_cnt, c_cnt = 0, 0
    if w[0] in vow:
        v_cnt += 1
    else:
        c_cnt += 1
    for i in range(len(w)-1):
        if w[i] in vow and w[i+1] in vow:
            return False
        if w[i+1] in vow:
            v_cnt += 1
        else:
            c_cnt += 1
    if c_cnt > v_cnt:
        return True
    return False

def valid(w):
    w1 = ''.join('v' if ch in vow else 'c' for ch in w)
    return w1.count('c')>w1.count('v') and 'vv' not in w1
    
    
cnt = 0
for w in permutations(alpha, r=5):
    if valid(w): cnt += 1

print(cnt)
