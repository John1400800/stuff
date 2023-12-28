import pygame

w, n = tuple(map(int, input().split()))

pygame.init()
width = w * n * 2
# width += width/n
screen = pygame.display.set_mode([width]*2)
pygame.display.set_caption('мишень')

colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
f = 0

for i in range(n):
    pygame.draw.circle(
        screen, colors[f],
        (width / 2, width / 2),
        w * (i + 1), w)
    f = 0 if f == len(colors) - 1 else f + 1
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
