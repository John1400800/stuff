def to_camel_case(text: str):
    inp: list = text.replace('-', '_').split('_')

    if len(inp):
        return inp[0] + ''.join([s.capitalize() for s in inp[1:]])


print(to_camel_case('O_oo'))