with (open(r'Independent_work1\candies.txt', 'r', encoding='utf-8') as f,
      open(r'Independent_work1\secret.txt', 'w', encoding='utf-8') as fw):
    lst = f.readline().rstrip().split()
    symbols = list(f.readline().rstrip())
    res = []
    for w in lst:
        for s in symbols:
            if s.lower() in w.lower():
                res.append(w.capitalize())
                break
    if res:
        fw.write(', '.join(res))
    else:
        fw.write('None')