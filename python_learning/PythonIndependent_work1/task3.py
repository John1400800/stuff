class NoInputError(Exception):
    pass


class ZeroNegativeError(Exception):
    pass


def journey_begins(*args: tuple[str, str], same_letters: int = 2) -> list[str]:
    if not args:
        raise NoInputError('No input data')
    if same_letters < 1:
        raise ZeroNegativeError('Invalid parameter value')

    res: list[str] = []
    for tpl in args:
        if not tpl[0] or not tpl[1]:
            raise ValueError('Empty value')

        set_comm_lett = set(tpl[0].lower()) & set(tpl[1].lower())
        if set_comm_lett and len(set_comm_lett) >= same_letters:
            # print(set_comm_lett)
            res.append(''.join(sorted(list(set_comm_lett))))

    return sorted(res)


# args = [('Foolish', 'food'), ('Solt', 'veruka'),
#         ('Beauregard', 'bubble gum'),
#         ('Teavee', 'television')]

# print(journey_begins(*args))
