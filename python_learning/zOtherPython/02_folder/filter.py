def foo_even_num(n: int) -> bool:
    return True if n % 2 == 0 else False


even_num = tuple(filter(lambda x: True if x % 2 == 0 else False, range(21)))
print(even_num)
