def valid(word):
    i = word.index("Ь")
    if i == len(word) - 1:
        return True
    elif i == 0:
        return False
    elif word[i+1] in ("А", "У"):
        return False
    return True

cnt = 0
for w in permutations("ВУАЛЬ", 5):
    if valid(w):
        cnt += 1

print(cnt)





