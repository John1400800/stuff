from string import digits, ascii_lowercase


def int_(lst, b):
    res = 0
    i, l = 0, len(lst)
    pow_ = l-1
    while i<l:
        res += lst[i]*b**pow_
        pow_ -= 1
        i += 1
    return res

b = False
for x in range(21):
    if b: break
    for y in range(21):
        r = int_((1,2,y,x,9),21)+int_((3,6,y,9,9),21)
        if r%18!=0:
             break
    else:
        print((int_((1,2,5,x,9),21)+int_((3,6,5,9,9),21))//18)
        b = True
        
        
        
