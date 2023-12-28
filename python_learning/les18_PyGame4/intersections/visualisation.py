import pygame
from intersection_straight_lines import intersection


pygame.init()
screen_size = 700, 500
screen = pygame.display.set_mode(screen_size)

p1, p2 = (100, 300), (500, 100)
p3, p4 = (500, 300), (400, 100)
pygame.draw.line(screen, "white", p1, p2, 2)
pygame.draw.line(screen, "white", p3, p4, 2)
if (intersect := intersection((p1, p2), (p3, p4))) != False:
    print(intersect)
    pygame.draw.circle(screen, "red", intersect, 4)
pygame.display.update()
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

pygame.quit()
