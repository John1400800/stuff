from itertools import product, permutations

def valid_99(word):
    if word[0] == "Ь":
        return False
    elif word.find("ЬА") != -1:
        return False
    elif word.find("ЬУ") != -1:
        return False
    return True

##cnt = 0
##for w in permutations("ВУАЛЬ", 5):
##    if valid(''.join(w)):
##        cnt += 1


def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res



##cnt = 0
##for w in product("СЛОН", repeat=5):
##    if w.count("С")==1:
##        cnt += 1

##cnt = 0     
##for w in product(('Е', 'Г', 'Э'), repeat=5):
##    if w[0] in ('Е', 'Э'):
##        cnt += 1



for i, w in enumerate(product(('А', 'О', 'У'), repeat=5)):
    if i+1 == 240:
        print(w)
        break



        
