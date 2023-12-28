def find_key(box):
    find = False
    def rec(lst):
        nonlocal find
        for el in lst:
            if find: break
            if el == 'key':
                find = True
            else:
                rec(el)
    rec(box)
    return find

box = [[], [], [[], [[], []], []]]
print(find_key(box))
