# recursion
def palindrom(s: str):
    if len(s)<=1:
        return True
    elif s[0]==s[-1]:
        return palindrom(s[1:-1])
    else:
        return False

def rec1(s):
    if len(s) in (1, 2):
        return s
    return '{}({}){}'.format(s[0], rec1(s[1:-1]), s[-1])

def pow_(x, p):
    if p==0:
        return 1
    if p<0:
        return 1/pow_(x, -p)
    elif p%2==0:
        return pow_(x, p//2)*pow_(x, p//2)
    else:
        return pow_(x, p-1)*x

def flatten(lst):
    for item in lst:
        if type(item)==list:
            for x in flatten(item):
                yield x
        else:
            yield item
            
lst1 = [1, [2, [3, 4, [5, 6], 7], 8], 9]
print(list(flatten(lst1)))
    
            
        
