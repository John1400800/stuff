import pygame
sc_size = 600, 400
cell_size = 58, 42

field = [
    [3, 3, 0, 3, 3, 3, 3, 3, 3, 3],
    [0, 0, 0, 0, 0, 3, 3, 0, 0, 0],
    [3, 3, 0, 3, 0, 0, 0, 0, 3, 0],
    [3, 3, 0, 0, 0, 3, 0, 3, 3, 0],
    [3, 0, 0, 3, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start_field = ((sc_size[0]-max(map(len, field))*cell_size[0])/2,
               (sc_size[1]-len(field)*cell_size[1])/2)

cord = [1, 1]
walk = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}

running = True
pygame.init()
sc = pygame.display.set_mode(sc_size)
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            click_btn = ev.unicode
            print(click_btn)
            if click_btn in walk.keys():
                new_cord = cord[0] + \
                    walk[click_btn][0], cord[1] + walk[click_btn][1]
                print(new_cord, end='   ')
                if (0 <= new_cord[1] < len(field) and
                    0 <= new_cord[0] < len(field[new_cord[1]]) and
                        field[new_cord[1]][new_cord[0]] != 3):
                    # очщяем предидущию клетку
                    field[cord[1]][cord[0]] = 0
                    cord = new_cord
                else:
                    print("Nope")

    sc.fill("white")
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell != 3:
                color = "yellow" if cell else "black"
                pygame.draw.rect(sc, color,
                                 (start_field[0]+cell_size[0]*x,
                                  start_field[1]+cell_size[1]*y,
                                  *cell_size))
    pygame.display.update()
    # логика
    field[cord[1]][cord[0]] = 1
pygame.quit()
