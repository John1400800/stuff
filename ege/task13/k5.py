lst = []
def rec(s, e):
    global lst
    if s[-1]==e:
        lst.append(s) if valid(s) else 0
    else:
        for p in dct[s[-1]]:
            rec(s+p, e)

def valid(w):
    return 'Ж' in w


s = 'АВБГ БЖЕ ВЗД ГЕИ ДЗЖ ЕЖИ ЖИ ЗИ ИКЛМ КНЛ ЛН МН Н'
dct = {p[0]:p[1:] for p in s.split()}
rec('А', 'Н')
print(lst, len(lst))
