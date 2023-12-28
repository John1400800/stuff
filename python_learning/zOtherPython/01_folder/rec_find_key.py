def find_key(el, level=0):
    if type(el)==list:
        return any(find_key(i) for i in el)
    elif el == 'key':
        return True
    return False

lst = [[], [], [[], []]]
print(find_key(lst))
