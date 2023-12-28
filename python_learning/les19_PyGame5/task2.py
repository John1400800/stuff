import os
from random import choice, randint
import pygame


def load_image(name: str) -> pygame.Surface:
    fullname = f"data\\{name}"
    if not os.path.isfile(fullname) or fullname[-4:] != ".png":
        raise Exception(f"file named {name} not found or file not png")
    else:
        image = pygame.image.load(fullname)
        image.set_colorkey(image.get_at((0, 0)))
        return image


def teleport(pos_abobus: list[int],
             window_size: tuple[int, int],
             size_abobus: tuple[int, int]
             ) -> list[int]:
    new_pos = pos_abobus.copy()

    if 0 > pos_abobus[0]:
        new_pos[0] = window_size[0]-size_abobus[0]
    elif pos_abobus[0] > window_size[0]-size_abobus[0]:
        new_pos[0] = 0
    if 0 > pos_abobus[1]:
        new_pos[1] = window_size[1]-size_abobus[1]
    elif pos_abobus[1] > window_size[1]-size_abobus[1]:
        new_pos[1] = 0
    return new_pos


window_size = width, height = 500, 400
pygame.init()
screen = pygame.display.set_mode(window_size)


image_abobus = load_image("creature.png")
size_abobus = image_abobus.get_size()
pos_abobus = [0, 0]

a = 1
one_step = 60
steps = {"w": (0, -one_step),
         "a": (-one_step, 0),
         "s": (0, one_step),
         "d": (one_step, 0)}
pressed = False
running = True
clock = pygame.time.Clock()
fps = 144
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.unicode in steps.keys():
                step_x, step_y = steps[ev.unicode][0], steps[ev.unicode][1]
                pressed = True
        elif ev.type == pygame.KEYUP:
            pressed = False
            a = 1
    if pressed:
        a += 0.01 if a < 3.5 else 0
        pos_abobus[0] += step_x*a/fps
        pos_abobus[1] += step_y*a/fps
    pos_abobus = teleport(pos_abobus, window_size, size_abobus)
    screen.fill("white")
    screen.blit(image_abobus, pos_abobus)
    pygame.display.update()

    clock.tick(fps)
pygame.quit()
