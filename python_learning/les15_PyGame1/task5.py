import pygame

n = int(input())

pygame.init()
w = 300  # 300
w_cell = w / n
screen = pygame.display.set_mode([w]*2)
pygame.display.set_caption('сфера')

color = (255, 0, 0)
width = 3
pygame.draw.circle(screen, [255]*3, [w / 2]*2, w/2)
for i in range(n):
    pygame.draw.ellipse(
        screen, color, (w_cell * i / 2, 0, w - w_cell * i, w), width)
    pygame.draw.ellipse(
        screen, color, (0, w_cell * i / 2, w, w - w_cell * i), width)
    color = [0]*3
    width = 1
pygame.draw.line(screen, color, (w / 2, 0), (w / 2, w), 1)
pygame.draw.line(screen, color, (0, w / 2), (w, w / 2), 1)
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
