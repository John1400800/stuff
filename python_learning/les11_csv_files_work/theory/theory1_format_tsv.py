# TSV
with open(r'les11_csv_files_work\theory\ikea.txt', 'r', encoding='utf-8') as txt_f:
    data = txt_f.read()

# Первые 10 строк
# for row in data.split('\n')[:10]:
#     print(row.split('\t'))

# Двумерный список
table = [row.split('\t') for row in data.split('\n')]
# Заголовки
keys = table.pop(0)
# Сортируем по цене
table = sorted(table, key=lambda lst: int(lst[1]))
print([st.capitalize() for st in keys])
print(*table[:20], sep='\n')
