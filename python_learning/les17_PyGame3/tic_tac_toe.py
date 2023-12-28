import pygame

field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
sep = '\n' + '  — '*max(map(len, field)) + '\n'

sc_size = 500, 400
cell_size = 100, 100
start_field = ((sc_size[0] - cell_size[0]*max(map(len, field)))/2,
               (sc_size[1] - cell_size[1]*len(field))/2)
radius = min(cell_size)/2 - 0.1*min(cell_size)

pygame.init()
sc = pygame.display.set_mode(sc_size)

isX = 1
is_win = 0
res_print = [0, "x win", "y win", "draw", True]

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            pos_click = [int((pos - start_field[i])//cell_size[i])
                         for i, pos in enumerate(ev.pos)]
            if (0 <= pos_click[1] < len(field) and
                    0 <= pos_click[0] < len(field[pos_click[1]]) and
                    not is_win):
                if not field[pos_click[1]][pos_click[0]]:
                    field[pos_click[1]][pos_click[0]] = "x" if isX else "o"
                    isX = not isX
                print(pos_click)
                print(sep, end='')
                print(sep.join(['| ' + ' | '.join([str(v) if v else ' 'for v in row]) + ' |'
                                for row in field]), end='')
                print(sep)

    sc.fill("white")
    for y, row in enumerate(field):
        for x, v in enumerate(row):
            pygame.draw.rect(sc, "black",
                             (start_field[0] + x*cell_size[0],
                              start_field[1] + y*cell_size[1],
                              *cell_size), 1)
            if v == 'x':
                pygame.draw.line(
                    sc, "blue",
                    ((start_field[0]+cell_size[0]*x)+(cell_size[0]-radius*2)/2,
                     (start_field[1]+cell_size[1]*y)+(cell_size[1] - radius*2)/2),
                    ((start_field[0]+cell_size[0]*(x+1))-(cell_size[0] - radius*2)/2,
                     (start_field[1]+cell_size[1]*(y+1))-(cell_size[1] - radius*2)/2),
                    int(min(cell_size)*0.16))
                pygame.draw.line(
                    sc, "blue",
                    ((start_field[0]+cell_size[0]*(x+1))-(cell_size[0] - radius*2)/2,
                     (start_field[1]+cell_size[1]*y)+(cell_size[1] - radius*2)/2),
                    ((start_field[0]+cell_size[0]*x)+(cell_size[0] - radius*2)/2,
                     (start_field[1]+cell_size[1]*(y+1))-(cell_size[1] - radius*2)/2),
                    int(min(cell_size)*0.16))
            elif v == "o":
                pygame.draw.circle(
                    sc, "red",
                    (start_field[0]+cell_size[0]*x+cell_size[0]/2,
                     start_field[1]+cell_size[1]*y+cell_size[1]/2),
                    radius, int(min(cell_size)*0.12))
    pygame.display.update()
    # логика на 3X3
    if not is_win:
        for i in range(len(field)):
            combo = (set(field[i]), set([row[i] for row in field]),
                     set([field[row][row] for row in range(len(field))]),
                     set([field[::-1][row][row] for row in range(len(field))]))
            if {"x"} in combo:
                is_win = 1
                break
            elif {"o"} in combo:
                is_win = 2
                break
            elif 0 not in [v for row in field for v in row]:
                is_win = 3
                break
    elif is_win:
        if is_win == 1:
            win_symb = "x"
        elif is_win == 2:
            win_symb = "o"
        else:
            win_symb = 0

        for y in range(len(field)):
            for x in range(len(row)):
                field[y][x] = win_symb
        if res_print[3]:
            print(res_print[is_win])
            res_print[3] = False

pygame.quit()
