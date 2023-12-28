# Замыкания

def main_func(name: str):
    def inner_func():
        nonlocal name
        print(f'Hello my friend {name}')

    return inner_func


# В разных областях видимости храняться разные переменные,
# в этом идея замыкания
a = main_func('Nikita')
a()
b = main_func('Artem')
b()
