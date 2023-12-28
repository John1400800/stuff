import pygame

colors = ('#FFC740', '#FF8B40')
w = 600
diagonal = w  # int(input())


def diamonds(screen: pygame.Surface, w: int, diagonal: int):
    '''многоугольники'''
    half_diag = diagonal // 2
    n = w // diagonal
    for i in range(n):
        for j in range(n):
            a = (diagonal*j, diagonal*i + half_diag)
            b = (diagonal*(j + 1), a[1])
            c = (diagonal*j + half_diag, diagonal*i)
            d = (c[0], diagonal*(i+1))
            pygame.draw.polygon(screen, colors[1],
                                (a, c, b, d))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode([w]*2)

while pygame.event.wait().type != pygame.QUIT:
    screen.fill(colors[0])
    if diagonal >= 30:
        diamonds(screen, w, diagonal)
        diagonal -= 1
pygame.quit()
