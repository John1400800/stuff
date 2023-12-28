from string import digits, ascii_lowercase



for x in (digits+ascii_lowercase)[:15]:
    r = int('135%s7'%x, 15)+int('7%s531'%x, 15)
    if r%14==0:
        print(r//14)
        break


##for x in range(15):
##    a1 = 1*15**4 + 3*15**3 + 5*15**2 + x*15 + 7
##    a2 = 7*15**4 + x*15**3 + 5*15**2 + 3*15 + 1
##    r = a1 + a2
##    if r%14==0:
##        print(r//14)
##        break
