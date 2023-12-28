# Обычная функция:
from turtle import st


def f():
    return [1, 2, 3, 5]


# Функция генератор:

def range2(*args):
    start = args[0] if len(args) > 1 else 0
    end = args[1] if len(args) > 1 else args[0]
    step = args[2] if len(args) > 2 else 1
    if step > 0:
        assert end > start, 'начало больше конца!!'
    elif step < 0:
        assert end < start, 'шаг отрицательный должно быть start < end'
    else:
        raise AssertionError('шаг не может быть нулевым')

    while start != end:
        yield start
        start += step


for i in range(10, 2, -1):
    print(i)

print()

for i in range2(10, 2, -1):
    print(i)
