dct = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}


def recode(line: str):
    for i in dct:
        line = line.replace(i, dct[i])
        line = line.replace(i.upper(), dct[i].title())
    return line


if __name__ == "__main__":
    with (open('cyrillic.txt', 'r', encoding='utf-8') as f1,
          open('transliteration.txt', 'w') as f2):
        for line in f1:
            f2.write(recode(line))
