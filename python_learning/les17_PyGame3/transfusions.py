import pygame
sc_size = 500, 400
cell_size = 20, 20

field = [[0 for _ in range(20)] for _ in range(18)]
field_start = ((sc_size[0]-max(map(len, field))*cell_size[0])/2,
               (sc_size[1]-len(field)*cell_size[1])/2)

cord = [0, 0]
in_step = 16
# прибавление
walk = {"w": (0, -in_step), "a": (-in_step, 0),
        "s": (0, in_step), "d": (in_step, 0)}

running = True
pygame.init()
sc = pygame.display.set_mode(sc_size)
walked = False
clock = pygame.time.Clock()
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN and ev.unicode in walk.keys():
            pressed_btn = ev.unicode
            walked = True
        elif ev.type == pygame.KEYUP and ev.unicode in walk.keys():
            walked = False

    sc.fill("white")
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            # отрисовка поля
            if cell >= 0:
                pygame.draw.rect(sc, "black",
                                    (field_start[0]+cell_size[0]*x,
                                    field_start[1]+cell_size[1]*y,
                                    *cell_size))
            # отрисовка квадратика
            pygame.draw.rect(sc, "yellow",
                                (field_start[0]+cell_size[0]*int(cord[0]),
                                field_start[1]+cell_size[1]*int(cord[1]),
                                *cell_size))

    pygame.display.update()
    clock.tick(60)
    # логика
    if walked:
        new_cord = [(cord[i] + walk[pressed_btn][i]/60) for i in range(2)]
        if (0 <= int(new_cord[1]) <= len(field)-1 and
                0 <= int(new_cord[0]) <= len(field[int(new_cord[1])])-1 and
                field[int(new_cord[1])][int(new_cord[0])] != -1):
            cord = new_cord
pygame.quit()
