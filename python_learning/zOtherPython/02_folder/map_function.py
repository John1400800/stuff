# Функция map является итератором!

a = [-1, 2, -3, 4, 5]
b = map(abs, a)  # Эквиволентно -->  b = [abs(el) for el in a]
print(list(b))

c = map(lambda a: a**2, a)
print(list(c))

lst = ['hello', 'hi', 'good morning', 'bye-bye']
d = map(str.upper, lst)  # Или -->  d = map(lambda sym: sym.upper(), lst)
print(*d, sep=', ')


d = map(lambda s: s + '!', lst)
print(*d)


# интересный пример!
k = map(lambda el: ''.join(sorted(el)), lst)
print(*k, sep=', ')

s = filter(lambda n: n % 2 == 0, map(int, input().split()))
print(*s, sep=', ')