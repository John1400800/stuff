class HumanSize:
    UNITS = ('B', 'KB', 'MB', 'GB', 'TB')

    def __init__(self, size: str) -> None:
        self.size = size
        if len(str(size).split()) < 2:
            self.size = f'{size} B'
        self.bytes = self.get_bytes()

    def get_bytes(self) -> float:
        size, unit = self.size.split()
        return (
            float(size) * 2 ** (self.UNITS.index(unit) * 10))

    def format(self):  # -> None | str:
        num = self.bytes
        for unit in self.UNITS:
            if abs(num) < 1024.0:
                return f'{round(num)} {unit}'
            num /= 1024.0


def foo(lst: list) -> dict:
    lst_f = []
    for s in lst:
        s_split = s.split()[0], ' '.join(s.split()[1:])   # Данные о файле
        extent = s_split[0][s_split[0].find('.') + 1:]  # Расширение файла

        # Добавления расширения в список расширений кнему список под данные о файлах
        if extent not in [el[0] for el in lst_f]:
            lst_f.append([extent, [], 0])

        # Добавления в список для данных данные о файле
        for indx, elem in enumerate(lst_f):
            if elem[0] == extent:
                lst_f[indx][1].append(s_split)
                lst_f[indx][2] += HumanSize(s_split[1]).get_bytes()
                break

    lst_f = sorted(
        [(i[0], sorted(i[1], key=lambda lst: lst[0]), HumanSize(i[2]).format())
         for i in lst_f],
        key=lambda lst: lst[0])

    # dct = {i[0]: (i[1], HumanSize(i[2]).format()) for i in lst_f}
    return lst_f


if __name__ == '__main__':
    with (open('input.txt', 'r') as inpf,
          open('output.txt', 'w') as outf):
        # print(foo(inpf))

        res = foo(inpf)
        for i in res:
            # print(i[0], i[1], i[2], sep='\n', end='\n\n')
            outf.write('\n'.join([i[0] for i in i[1]]) + '\n')
            outf.write('----------\n')
            outf.write(f'Summary: {i[2]}\n\n')
