from random import sample
from unicodedata import name


def read_name_surname(
    f_name: str
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    '''чтение имён и фамилий из файла f_name\n
    преобразование имён и фамилий в два разных кортэжа'''
    
    f = open(f_name)
    f.readline() #считываем первую строку где написанно names:
    string = f.read()
    f.close()

    string = string.replace('\r', '').replace('\n', '').replace('\t', '')
    names, surnames = [tuple(block.split(', '))
                       for block in string.split('surnames:')]

    return names, surnames


def full_names(names: tuple, surname: tuple) -> list[str]:
    pass


if __name__ == '__main__':
    f_name_with_names_surnames = r'projectPyQt\test_db\names_surnames.txt'
    names, surnames = [
        sample(tpl, 5)
        for tpl in read_name_surname(f_name_with_names_surnames)
    ]
    print(names, surnames, sep='\n\n')
