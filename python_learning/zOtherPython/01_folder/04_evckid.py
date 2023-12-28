# fast
def evclid(a, b):
    if a>b: a, b = b, a
    while a:
        a, b = b%a, a
    return b

# fast
def rec_evclid(a, b):
    if a>b: a, b = b, a
    if b%a==0:
        return a
    return rec_evclid1(a, b%a)

# slow
def rec_evclid1(a, b):
    if a==b:
        return a
    if a>b: a, b = b, a
    return rec_evclid(a, b-a)

# slow
def evclid1(a, b):
    while a != b:
        if a>b: a, b = b, a
        b = b-a
    return a


