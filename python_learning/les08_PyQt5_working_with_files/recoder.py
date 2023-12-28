TRANSCRIPT = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
              "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
              "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
              "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
              "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
              "б": "b", "ю": "ju", "ё": "jo"}


with (open('cyrillic.txt', 'r', encoding='utf-8') as file1,
      open('transliteration.txt', 'w') as file2):
    for row in file1:
        for sym in row:
            if sym.lower() in TRANSCRIPT.keys():
                trnskrpt = TRANSCRIPT[sym.lower()]
                if sym.isupper():
                    file2.write(trnskrpt.capitalize())
                else:
                    file2.write(trnskrpt)
            else:
                file2.write(sym)
