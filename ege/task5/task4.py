for x in range(10, 100):
    y = ''
    for i in (2, 3, 5):
        y += str(x % i)
    if y == '104':
        print(x)
        break
