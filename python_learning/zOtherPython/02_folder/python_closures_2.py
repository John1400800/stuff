# Замыкания пример 2

def adder(value):

    def inner(a) -> int:
        return value + a

    return inner


# f1 = adder(1)
# print(f1(3))

# f2 = adder(2)
# print(id(f1), id(f2), sep='\n')

# f3 = adder(2)(3)
# print(f3)

# Ещё один пример замыкания:

def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


c = counter()
print(c())
print(c())
print(c())
print(c())
