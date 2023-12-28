REGARDING = ((0, -1), (-1, 0), (0, 1), (1, 0))

field = [[0,  0,  0, -1,  0,  0],
         [0, -1,  0,  0, -1,  0],
         [0,  0, -1,  0,  0,  0],
         [0,  0,  0,  0,  0,  0]]
start_pos = (1, 0)
end_pos = (4, 0)
weight = 0

paths = [start_pos]
new_paths = []
while_brake = True

while while_brake:
    for x, y in paths:
        for step_x, step_y in REGARDING:
            new_x, new_y = x+step_x, y+step_y
            if (0 <= new_x < len(field[0]) and
                0 <= new_y < len(field) and
                field[new_y][new_x] == 0 and
                (new_x, new_y) != start_pos and
                    (new_x, new_y) != end_pos):
                new_paths.append((new_x, new_y))
                field[new_y][new_x] = weight+1
            elif (new_x, new_y) == end_pos:
                field[new_y][new_x] = weight+1
                while_brake = False
    paths = new_paths.copy()
    weight += 1


path_cord = [end_pos]
while path_cord[-1] != start_pos:
    on_cord = path_cord[-1]
    on_cell_v = field[on_cord[1]][on_cord[0]]
    for step_x, step_y in REGARDING:
        new_x, new_y = on_cord[0]+step_x, on_cord[1]+step_y
        go_cell_v = field[new_y][new_x]
        if 0 <= new_x < len(field[0]) and 0 <= new_y < len(field) and go_cell_v < on_cell_v and go_cell_v != -1:
            path_cord.append((new_x, new_y))
            break
    # print(path_cord)

def cell_draw(v) -> str:
    if v == -1:
        return '#'
    elif v == '*':
        return v
    else:
        return ' '

idx = 0
path_cord = path_cord[::-1]
while not input(f'{"  — "*len(field[0])}') and idx<len(path_cord):
    field[path_cord[idx][1]][path_cord[idx][0]] = '*'
    print(('\n'+f'{"  — "*len(field[0])}'+'\n').join(
        ['| ' + ' | '.join(map(lambda v: cell_draw(v), row))
        + ' |' for row in field]
    ), sep='\n')
    idx += 1


