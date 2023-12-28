import functools


def moves(s):
    return s + 2, s*2


@functools.lru_cache(None)
def game(s):
    if s >= 25:
        return 'W'
    if any(game(v) == 'W' for v in moves(s)):
        return 'P1'
    if all(game(v) == 'P1' for v in moves(s)):
        return 'B1'
    if any(game(v) == 'B1' for v in moves(s)):
        return 'P2'
    if all(game(v) == 'P1' or game(v) == 'P2' for v in moves(s)):
        return 'B2'
    