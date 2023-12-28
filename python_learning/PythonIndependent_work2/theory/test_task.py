import sys
import csv


years, *balance = [s.rstrip() for s in sys.stdin.readlines()]
years = tuple(map(int, years.split()))
balance = {s.split(': ')[0]: int(s.split(': ')[1]) for s in balance}

# подключение к файлу
with open(r"f.csv") as csv_f:
    reader = csv.DictReader(csv_f, delimiter=';', quotechar='"')
    # вычитание из баланса затрат из таблицы
    for dct in reader:
        if ((years[1] >= int(dct['year']) >= years[0]) and
                dct['name'] in balance.keys()):
            balance[dct['name']] -= int(dct['cost'])

print(*[f'{name}: {balance}' for name,
      balance in balance.items()], sep='\n')
