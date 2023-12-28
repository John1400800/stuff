import csv


with (
    open(r'les11_csv_files_work\theory\ikea.csv', encoding='utf-8')
    as
    csv_file
):
    reader = csv.DictReader(csv_file, delimiter=';', quotechar='"')
    expensive = [dct for dct in sorted(
        reader, key=lambda dct: int(dct['price']), reverse=True)]

    print(*expensive[:10], sep='\n')
