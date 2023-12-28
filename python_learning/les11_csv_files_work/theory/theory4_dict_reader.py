import csv

data = (
    {
        'lastname': 'Иванов',
        'firstname': 'Пётр',
        'class_number': 8,
        'class_letter': 'A'
    },
    {
        'lastname': 'Кузнецов',
        'firstname': 'Алексей',
        'class_number': 8,
        'class_letter': 'B'
    },
    {
        'lastname': 'Меньшова',
        'firstname': 'Алиса',
        'class_number': 8,
        'class_letter': 'B'
    },
    {
        'lastname': 'Антанесян',
        'firstname': 'Никита',
        'class_number': 8,
        'class_letter': 'A'
    }
)

with open(
        file=r'les11_csv_files_work\theory\dictwriter.csv',
        mode='w',
        encoding='utf-8',
        newline=''
) as csv_file:

    writer = csv.DictWriter(
        f=csv_file,
        fieldnames=data[0].keys(),
        delimiter=';',
        quoting=csv.QUOTE_NONNUMERIC
    )

    writer.writeheader()

    for dct in data:
        writer.writerow(dct)
