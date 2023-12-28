from itertools import product

cnt = 0
for s in product(range(8), repeat=5):
    if s[0]==0 or s.count(4) != 2:
        continue
    for i in range(len(s)):
        if s[i] == 4:
            if int(*s[i-1:i])%2 or int(*s[i+1:i+2])%2:
                break
    else:
        cnt += 1

print(cnt)
            
            
    
