txt1 = []
txt2 = []
while (n := input())  != '':
    txt1.append(n)

while (n := input()) != '':
    txt2.append(n)

txt1, txt2 = ''.join(txt1), ''.join(txt2)

def antiplag(txt1: str, txt2: str):
    len_small_txt = min(map(len, (txt1, txt2)))

    cnt = 0
    for i in range(len_small_txt):
        if txt1[i] == txt2[i]:
            cnt += 1

    percent = round((cnt / len_small_txt), 2) * 100
    return percent


    

# print(txt1, txt2, percent, sep='\n\n')


