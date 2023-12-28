import pygame
from random import randint
from path_beta import return_path

# field = [[-1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1],
#          [0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
#          [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0],
#          [0, -1, 0,  0, 0, -1, 0, 0, 0, -1, -1, 0],
#          [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, 0],
#          [0, -1, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0],
#          [0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, 0]]
w, h = map(int, input('Введите размер поля в клетках ширина высота:\n').split())
field = [[-1 if randint(0, 18) == 3 else 0 for _ in range(w)] for _ in range(h)]
while True:
    pos = tuple(map(int, input('введите положение:\n').split()))
    if len(pos) == 2 and 0<=pos[0]<len(field[0]) and 0<=pos[1]<len(field) and field[pos[1]][pos[1]] != -1:
        break
    else:
        print('неправильное расположение')



def render(sc: pygame.Surface, field: list[list[int]]):
    sc.fill("black")
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == -1:
                pygame.draw.rect(
                    sc, "white",
                    (cell_size*x+1, cell_size*y+1,
                     *[cell_size-2]*2),
                    border_radius=int(cell_size*0.1))
            if pos == (x, y):
                pygame.draw.rect(
                    sc, "red",
                    (cell_size*x+1, cell_size*y+1,
                     *[cell_size-2]*2),
                    border_radius=int(cell_size*0.1))
    pygame.display.update()


cell_size = int(600/max(w, h))
last_pos = ()

pygame.init()
sc = pygame.display.set_mode((len(field[0])*cell_size, len(field)*cell_size))
clock = pygame.time.Clock()
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONUP:
            click_pos = tuple([int(p/cell_size) for p in ev.pos])
            if (0 <= click_pos[0] < len(field[0]) and
                0 <= click_pos[1] < len(field) and
                    field[click_pos[1]][click_pos[0]] != -1):
                path = return_path(pos, click_pos, field)
                # print(pos, click_pos, path)
                if path:
                    for cord in path:
                        pos = cord
                        render(sc, field)
                        clock.tick(8)
                

    render(sc, field)
pygame.quit()
