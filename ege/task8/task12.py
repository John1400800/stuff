from itertools import product


n = 1 
alpha = sorted('мангуст')
for i, w in enumerate(product(alpha, repeat=6), 1):
    if w[0] != 'у' and w.count('м')==2 and w.count('г')<=1:
        n = i

print(n)
        
