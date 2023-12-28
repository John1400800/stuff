# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def like_this2(names: list) -> str:
    n = len(names)
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {} others like this"}

    if n < 4:
        return d[n].format(*names)
    return d[4].format(*names[:2], len(names[2:]))


def like_this(names: list) -> str:
    likes_this = len(names)
    ending1 = ' likes this'
    ending2 = ' like this'
    ending3 = ' others like this'
    if likes_this == 0:
        res = 'no one' + ending1
    elif likes_this == 1:
        res = names[0] + ending2
    elif likes_this == 2:
        res = ' and '.join(names) + ending2
    else:
        res = (', '.join(names[:2]) + ' and '
               + (names[2] + ending2 if len(names[2:]) == 1
                  else str(len(names[2:])) + ending3))
    return res


print(like_this2([]))
print(like_this2(["Peter"]))
print(like_this2(["Jacob", "Alex"]))
print(like_this2(["Max", "John", "Mark"]))
print(like_this2(["Alex", "Jacob", "Mark", "Max"]))
print(like_this2(["Alex", "Jacob", "Mark", "Max", "Oleg"]))
