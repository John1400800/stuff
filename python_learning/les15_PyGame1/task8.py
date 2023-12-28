import sys
from random import randint
import pygame


def drow_cube(a, w, screen: pygame.Surface, color1: pygame.Color) -> None:
    color2, color3 = pygame.Color(0, 0, 0), pygame.Color(0, 0, 0)
    color2.hsva = (color1.hsva[0], 100, 100)
    color3.hsva = (color1.hsva[0], 100, 50)

    pygame.draw.rect(screen, color1, (a[0], a[1], w, w))
    pygame.draw.polygon(
        screen, color2,
        (a,
         (a[0]+w*0.5, a[1]-w*0.5),
         (a[0]+1.5*w, a[1]-w*0.5),
         (a[0]+w, a[1])))
    pygame.draw.polygon(
        screen, color3,
        ((a[0]+w, a[1]),
         (a[0]+w*1.5, a[1]-w*0.5),
         (a[0]+w*1.5, a[1]+w*0.5),
         (a[0]+w, a[1]+w))
    )
    # pygame.display.flip()


w, h = tuple(map(int, input().split()))
# a = ((300-w)*0.5, (300-w)*0.5+w*0.5)

if any((w % 4 != 0, w > 100)):
    print('Error')
    pygame.quit()
    sys.exit()

pygame.init()
screen = pygame.display.set_mode((700, 300))

color = pygame.Color(0, 0, 0)
color.hsva = (h, 100, 75)

# drow_cube(a, w, screen, color)

running = True
a = [0, (300-w)*0.5+w*0.5]
v = 60  # движение в секунду
fps = 24 # кадры в секунду
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    drow_cube(a, w, screen, color)
    pygame.display.flip()
    if a[0] >= 700 - w:
        a[0] = 0
    else:
        a[0] += v / fps
        clock.tick(fps)
        print(a[0])
pygame.quit()
