lst = (17, 34, 41, 45, 57, 67, 81, 93, 98)
s = 41

def search_rec(s, lst, l=0, h=len(lst)) -> int:
    m = (l+h)//2
    if lst[m] == s:
        return m
    elif lst[m] < s:
        return search(s, lst, m, h)
    elif lst[m] > s:
        return search(s, lst, l, m)

def search(s, lst):
    l, h = 0, len(lst)-1
    while True:
        m = (l+h)//2
        if lst[m] == s:
            break
        elif lst[m] > s:
            h = m
        else:
            l = m
    return m
    

# print(search(s, lst))
print(search_rec(s, lst))

