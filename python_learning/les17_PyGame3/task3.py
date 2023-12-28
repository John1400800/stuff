from random import randint
import pygame
# n_cells = int(input())
n_cells = 7

field = [[randint(0, 1) for _ in range(n_cells)] for _ in range(n_cells)]
print(*field, sep='\n')

sc_size = 600, 400
cell_size = (min(sc_size)-60) / n_cells
field_start = ((sc_size[0] - cell_size*n_cells) / 2,
               (sc_size[1] - cell_size*n_cells)/2)

pygame.init()
sc = pygame.display.set_mode(sc_size)
motion = 0
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            click_pos = [int((p-field_start[i])//cell_size)
                         for i, p in enumerate(ev.pos)]
            if (all([0 <= p < n_cells for p in click_pos]) and
                    (v := field[click_pos[1]][click_pos[0]]) == motion):
                for i in range(n_cells):
                    field[i][click_pos[0]] = v
                    field[click_pos[1]][i] = v
                print(click_pos, v)
                motion = 1 if motion == 0 else 0

    sc.fill("black")
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            color = "red" if cell == 1 else "blue"
            start_cell = (field_start[0]+cell_size*x,
                          field_start[1]+cell_size*y)

            pygame.draw.rect(sc, "white",
                             (*start_cell,
                              *[cell_size]*2),
                             1)
            pygame.draw.circle(
                sc, color,
                [p+cell_size/2 for p in start_cell],
                (cell_size/2)*0.9)
    pygame.display.update()
    #
pygame.quit()
