import pygame

side, n = tuple(map(int, input().split()))

pygame.init()
screen = pygame.display.set_mode([side]*2)
pygame.display.set_caption("Шахматная доска")

f = True
for h in range(n):
    for w in range(n):
        color = tuple([0]*3 if f else [255]*3)
        f = not f
        pygame.draw.rect(
            screen, color,
            ((side / n) * w, (side / n) * h, side / n, side / n))
        pygame.display.flip()
    f = not f if n % 2 == 0 else f

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
