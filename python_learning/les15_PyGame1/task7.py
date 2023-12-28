import pygame
col_white, col_red = [255]*3, (255, 0, 0)

window_size = window_w, window_h = 300, 200
pygame.init()
screen = pygame.display.set_mode(window_size)

screen.fill(col_white)
for j in range(12):
    indent_y = 2 * j
    for i in range(10):
        indent_x = 2 * i
        difference = 15 if j % 2 != 0 else 0
        pygame.draw.rect(
            screen, col_red,
            ((30*i + indent_x) - difference, 15*j + indent_y, 30, 15))

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
