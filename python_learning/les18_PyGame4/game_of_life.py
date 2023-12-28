# оприделение рядом стоящих
def near(row_f, col_f, field: list[int]) -> int:
    regarding = ((-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1))
    n_cells = len(field)
    cnt = 0
    for (row, col) in regarding:
        if field[(row_f+row) % n_cells][(col_f+col) % n_cells]:
            cnt += 1
    return cnt


# отрисовка
def display(field: list[int]) -> str:
    display = ('  — '*n_cells+'\n'
               + '\n'.join(
                   [f"| {' | '.join(map(lambda v: ' ' if v == 0 else 'o', row))} |\n{'  — '*n_cells}"
                    for row in field]))
    return display


if __name__ == '__main__':
    # создание поля n_cells x n_cells клеток
    n_cells = 7
    field = [[0 for _ in range(n_cells)] for _ in range(n_cells)]

    field[0][0] = 1
    field[0][1] = 1
    field[0][2] = 1
    field[1][2] = 1
    field[2][1] = 1

    while not input('----'*n_cells):
        # отрисовка
        print(display(field))
        # логика
        new_field = [[0 for _ in range(n_cells)] for _ in range(n_cells)]
        for y, row in enumerate(field):
            for x, cell in enumerate(row):
                if cell:
                    if near(y, x, field) in (2, 3):
                        new_field[y][x] = 1
                else:
                    if near(y, x, field) == 3:
                        new_field[y][x] = 1
        field = [row.copy() for row in new_field]
