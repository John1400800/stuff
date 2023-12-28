# # Обычная функция:

# def f():
#     return [1, 2, 3, 5]


# # Функция генератор:

# def fgen():
#     s = 7
#     for i in [43, 65, 32]:
#         yield i
#         print(s)
#         s = s*10+7

# g = fgen()
# print(next(g))
# print(next(g))
# print(next(g))

# # s = fgen()
# # print(next(s))
# # print(next(s))
# # print(next(s))
# # print(next(s))
# # # print(next(s))

# # for i in fgen():
# #     print(i)

def fact(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        a.append(pr)
    return a


def fact2(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


a = fact2(10)
