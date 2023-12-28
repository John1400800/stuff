# Квадраты чисел
import csv


with (
        open(
            file=r'les11_csv_files_work\theory\squares_of_numbers.csv',
            mode='w',
            encoding='utf-8',
            newline='')
    as csv_file
):

    writer = csv.writer(
        csv_file,
        delimiter=';',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    for i in range(int(input('Введите число: '))):
        writer.writerow((i, i**2, 'Квадрат числа %d равен %d' % (i, i**2)))
