def dash(s: str):
    if '--' in s:
        return False
    elif s[0] == '-' or s[-1] == '-':
        return False
    return True

print(dash('12575-87279-122-'))
