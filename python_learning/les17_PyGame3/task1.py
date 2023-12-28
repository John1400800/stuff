import pygame
sc_size = 600, 400
num_cells = 4, 6
cell_size = 60, 50
field_start = ((sc_size[0] - (cell_size[0] * num_cells[0])) / 2,
               (sc_size[1] - (cell_size[1] * num_cells[1])) / 2)

field = [
    [0 for col in range(num_cells[0])]
    for row in range(num_cells[1])]
print(*field, sep="\n")

pygame.init()
sc = pygame.display.set_mode(sc_size)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            pos_click = [int((p - field_start[i]) // cell_size[i])
                         for i, p in enumerate(ev.pos)]
            if (0 <= pos_click[0] <= num_cells[0]-1 and
                    0 <= pos_click[1] <= num_cells[1]-1):
                for y in range(num_cells[1]):
                    for x in range(num_cells[0]):
                        if x == pos_click[0] or y == pos_click[1]:
                            field[y][x] += 1
                        field[y][x] %= 2

                print(pos_click)
            else:
                print(None)

    sc.fill("black")
    for y, row in enumerate(field):
        for x, v in enumerate(row):
            start = field_start[0] + x * \
                cell_size[0], field_start[1] + y*cell_size[1]
            border = 0 if v else 1
            pygame.draw.rect(sc, "white",
                             (start[0], start[1], *cell_size),
                             border)
    pygame.display.update()

pygame.quit()
