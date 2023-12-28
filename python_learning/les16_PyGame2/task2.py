import pygame
from random import randint
pygame.init()

size_w = w, h = randint(200, 800), randint(200, 600)

screen = pygame.display.set_mode(size_w)

fps = 220
v = 100
v_per_frame = v / fps
running = True
balls = []
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(*balls, sep="\n")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(pos)
            dct = {"x": {"pos": pos[0], "speed": -v_per_frame},
                   "y": {"pos": pos[1], "speed": -v_per_frame}}
            balls.append(dct)
    screen.fill('black')

    for ball in balls:
        pygame.draw.circle(
            screen, [255]*3,
            (ball["x"]["pos"], ball["y"]["pos"]),
            10)

        if ball["y"]["pos"] <= 10:
            ball["y"]["speed"] = -ball["y"]["speed"]
        elif ball["y"]["pos"] >= h - 10:
            ball["y"]["speed"] = -ball["y"]["speed"]
        elif ball["x"]["pos"] <= 10:
            ball["x"]["speed"] = -ball["x"]["speed"]
        elif ball["x"]["pos"] >= w - 10:
            ball["x"]["speed"] = -ball["x"]["speed"]

        ball["x"]["pos"] += ball["x"]["speed"]
        ball["y"]["pos"] += ball["y"]["speed"]

    pygame.display.flip()
    clock.tick(fps)
