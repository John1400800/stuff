from random import randint
import os
import pygame


def intersection(x1: int, x2: int, y1: int, y2: int, sprite_size: tuple[int]):
    return ((x1 > x2-sprite_size[0] and x1 < x2+sprite_size[0]) and
            (y1 > y2-sprite_size[1] and y1 < y2+sprite_size[1]))


def location_bombs(screen_size: tuple[int],
                   bomb_size: tuple[int],
                   cnt_bomb: int
                   ) -> list[tuple[int, int]]:
    bombs: list[tuple[int, int]] = []
    while cnt_bomb:
        x_pos, y_pos = (randint(0, screen_size[0]-bomb_size[0]),
                        randint(0, screen_size[1]-bomb_size[1]))
        # print(x_pos, y_pos)
        if all([not intersection(x_pos, x, y_pos, y, bomb_size)
                for x, y in bombs]) or not len(bombs):
            bombs.append((x_pos, y_pos))
            cnt_bomb -= 1

    return bombs


def load_img(name: str) -> pygame.Surface:
    path = f"data\\{name}"
    if os.path.isfile(path) and path[-4:] in (".png", ".jpg"):
        image = pygame.image.load(path)
        return image
    raise Exception('no file or wrong extension')


screen_size = 500, 400
bomb_image = load_img("bomb.png")
bomb_size = bomb_image.get_size()
boombs = location_bombs(screen_size, bomb_size, 37)

boom_image = load_img("boom.png")
boom = []

pygame.init()
screen = pygame.display.set_mode(screen_size)
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            for i, (x, y) in enumerate(boombs):
                if intersection(ev.pos[0], x, ev.pos[1], y, bomb_size):
                    boombs.pop(i)
                    boom.append([x, y, 30])
                    break

    screen.fill("black")
    for x, y in boombs:
        screen.blit(bomb_image, (x, y))
    for i, (x, y, sec) in enumerate(boom):
        screen.blit(boom_image, (x, y))
        boom[i][2] -= 0.4
    boom = list(filter(lambda tpl: tpl[2] > 0, boom))
    pygame.display.update()
pygame.quit()
