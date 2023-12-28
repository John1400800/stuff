import pygame

colors = ["white", "blue", "red"]

sc_size = 600, 400
num_cells = 12, 6
cell_size = 45, 45
field_start = ((sc_size[0] - (cell_size[0] * num_cells[0])) / 2,
               (sc_size[1] - (cell_size[1] * num_cells[1])) / 2)

# field = [
#     [0 for col in range(num_cells[0])]
#     for row in range(num_cells[1])]
field = [[0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]
print(*field, sep="\n")

pygame.init()
sc = pygame.display.set_mode(sc_size)

last_pos_click = 0
running = True
drawing = False
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos_click = [int((p - field_start[i]) // cell_size[i])
                              for i, p in enumerate(ev.pos)]
            if (0 <= last_pos_click[0] <= num_cells[0]-1 and
                    0 <= last_pos_click[1] <= num_cells[1]-1):
                field[last_pos_click[1]][last_pos_click[0]] += 1
                field[last_pos_click[1]][last_pos_click[0]] %= 3
                print(last_pos_click)
        elif ev.type == pygame.MOUSEMOTION:
            if drawing:
                pos_click = [int((p - field_start[i]) // cell_size[i])
                             for i, p in enumerate(ev.pos)]
                if (0 <= pos_click[0] <= num_cells[0]-1 and
                        0 <= pos_click[1] <= num_cells[1]-1 and last_pos_click != pos_click):
                    field[pos_click[1]][pos_click[0]] += 1
                    field[pos_click[1]][pos_click[0]] %= 3
                    print(pos_click)
                last_pos_click = pos_click

        elif ev.type == pygame.MOUSEBUTTONUP:
            drawing = False

    sc.fill("black")
    for y, row in enumerate(field):
        for x, v in enumerate(row):
            start = field_start[0] + x * \
                cell_size[0], field_start[1] + y*cell_size[1]
            border = 0 if v else 1
            pygame.draw.rect(sc, colors[v],
                             (start[0], start[1], *cell_size),
                             border)

            # if v:
            #     radius = min(sz/2 - sz*0.1 for sz in cell_size)
            #     pygame.draw.circle(sc, "white",
            #                        (start[0]+cell_size[0]/2,
            #                         start[1]+cell_size[1]/2),
            #                        radius, 4)
    pygame.display.update()

pygame.quit()
