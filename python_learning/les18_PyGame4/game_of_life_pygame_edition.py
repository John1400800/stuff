from game_of_life import near
import pygame
pygame.init()

screen_size = [600]*2
n_cell = 20
cell_size = screen_size[0] / n_cell, screen_size[1] / n_cell

field = [[0 for _ in range(n_cell)] for _ in range(n_cell)]
field[0][0] = 1
field[0][1] = 1
field[0][2] = 1
field[1][2] = 1
field[2][1] = 1

screen = pygame.display.set_mode(screen_size)
running = True
run = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "r":
                run = not run
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_cell = [int(p//cell_size[i])
                          for i, p in enumerate(event.pos)]
            field[click_cell[1]][click_cell[0]
                                 ] = 0 if field[click_cell[1]][click_cell[0]] else 1

    screen.fill("white")
    new_field = [[0 for _ in range(n_cell)] for _ in range(n_cell)]
    for y in range(n_cell):
        for x in range(n_cell):
            border = 1 if not field[y][x] else 0
            pygame.draw.rect(screen, "black",
                             (cell_size[0]*x, cell_size[1]*y,
                              *cell_size), border)
            if run:
                if field[y][x]:
                    if near(y, x, field) in (2, 3):
                        new_field[y][x] = 1
                else:
                    if near(y, x, field) == 3:
                        new_field[y][x] = 1

    field = [row.copy() for row in new_field] if run else field

    pygame.display.update()
    clock.tick(8)
pygame.quit()
